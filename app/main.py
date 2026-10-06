import streamlit as st
import pandas as pd
import plotly.express as px

from app.database import init_db, save_analysis, history, summary
from app.engine.detector import analyze_email
from app.engine.eml_parser import parse_eml
from app.ml_model import predict

st.set_page_config(page_title="Phishing Email Detection & Awareness", page_icon="🛡️", layout="wide")
init_db()

st.title("🛡️ Phishing Email Detection & Awareness Dashboard")
st.caption("Defensive, local-first educational project. Samples are analyzed locally; URLs are never opened or crawled.")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["Analyze Email", "Dashboard", "Awareness Center", "About"])
    st.divider()
    st.info("Use only synthetic or authorized sample emails. Never paste real passwords, OTPs, API keys, or confidential mail.")

def show_result(result):
    risk = result["risk"]
    score = risk["score"]
    label = risk["classification"]
    st.subheader("Risk Assessment")
    c1, c2, c3 = st.columns(3)
    c1.metric("Risk score", f"{score}/100")
    c2.metric("Classification", label)
    c3.metric("URLs found", len(result["url_analysis"]["urls"]))

    st.progress(score / 100)
    st.subheader("Why this result?")
    if risk["reasons"]:
        for reason in risk["reasons"]:
            st.write("• " + reason)

    st.subheader("Signal breakdown")
    breakdown = pd.DataFrame([
        {"Signal": "Content", "Score": risk["components"]["content"]},
        {"Signal": "URLs", "Score": risk["components"]["urls"]},
        {"Signal": "Sender", "Score": risk["components"]["sender"]},
    ])
    st.bar_chart(breakdown.set_index("Signal"))

    with st.expander("Detailed analysis"):
        st.json({
            "content_analysis": result["content_analysis"],
            "url_analysis": result["url_analysis"],
            "sender_analysis": result["sender_analysis"],
        })

    st.subheader("Recommended action")
    if score >= 70:
        st.error("Do not click links or provide information. Verify the request through a trusted channel and report the message to your organization.")
    elif score >= 40:
        st.warning("Treat the message cautiously. Verify the sender and destination independently before taking action.")
    else:
        st.success("No strong indicators were detected by the current rules. Continue normal email hygiene and verify unexpected requests.")

if page == "Analyze Email":
    st.header("Analyze a sample email")
    uploaded = st.file_uploader("Optional: upload a safe .txt or .eml sample", type=["txt", "eml"])
    sender = st.text_input("Sender", placeholder="security@example.test")
    subject = st.text_input("Subject", placeholder="Example security notification")
    body = st.text_area("Email content", height=240, placeholder="Paste synthetic email text here...")

    if uploaded:
        raw = uploaded.read()
        if uploaded.name.lower().endswith(".eml"):
            parsed = parse_eml(raw)
            sender = st.text_input("Parsed sender", value=parsed["sender"])
            subject = st.text_input("Parsed subject", value=parsed["subject"])
            body = st.text_area("Parsed body", value=parsed["body"], height=240)
        else:
            body = raw.decode("utf-8", errors="replace")
            st.text_area("Loaded text", value=body, height=180, disabled=True)

    if st.button("🔎 Analyze Email", type="primary"):
        if not body.strip() and not subject.strip():
            st.warning("Enter a subject or email body first.")
        else:
            result = analyze_email(sender, subject, body)
            save_analysis(result)
            show_result(result)

elif page == "Dashboard":
    st.header("Security Analytics Dashboard")
    s = summary()
    c1, c2 = st.columns(2)
    c1.metric("Emails analyzed", s["total"])
    c2.metric("Average risk score", s["average_score"])
    rows = history()
    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)
        counts = df["classification"].value_counts().reset_index()
        counts.columns = ["classification", "count"]
        fig = px.bar(counts, x="classification", y="count", title="Classification distribution")
        st.plotly_chart(fig, use_container_width=True)
        fig2 = px.histogram(df, x="score", nbins=10, title="Risk score distribution")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No analyses yet. Analyze a few synthetic samples to populate the dashboard.")

elif page == "Awareness Center":
    st.header("🎓 Phishing Awareness Center")
    topics = {
        "Red flags": [
            "Unexpected urgency or threats of account suspension.",
            "Requests for passwords, OTPs, gift cards, payments, or secrets.",
            "Links whose domain does not match the claimed organization.",
            "Unexpected attachments or unusual sender addresses.",
        ],
        "Verify safely": [
            "Do not use the phone number or link inside a suspicious message.",
            "Open the organization's known website manually or use a trusted contact.",
            "For work email, report suspicious messages through the approved reporting process.",
        ],
        "Password & MFA hygiene": [
            "Never share passwords or one-time codes.",
            "Use unique passwords and a password manager.",
            "Enable phishing-resistant MFA where available.",
        ],
        "Incident response": [
            "If you clicked a suspicious link, stop and report it promptly.",
            "If credentials were entered, change them using the legitimate site and notify the responsible security team.",
            "Preserve the sample email for authorized investigation; do not forward it to random recipients.",
        ],
    }
    for title, points in topics.items():
        with st.expander(title, expanded=True):
            for p in points:
                st.write("• " + p)

elif page == "About":
    st.header("About the project")
    st.markdown("""
**Purpose:** demonstrate defensive email-security engineering with explainable phishing detection.

**Core pipeline:**  
Email input → safe parsing → content analysis + URL analysis + sender analysis → weighted risk score → classification → explanation → SQLite history → analytics.

**Security boundaries:**  
- No links are visited.
- No credentials are collected.
- No phishing pages are generated.
- No real users or systems are targeted.
- Demonstrations should use synthetic `.txt`/`.eml` samples and reserved/example domains.

**Optional ML:** a local TF-IDF + Logistic Regression baseline can be trained from the included synthetic dataset. It is an educational classifier, not a replacement for enterprise email-security controls.
""")
