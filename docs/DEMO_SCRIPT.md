# 5-Minute Demo Script

1. Start the application with `python -m streamlit run app/main.py`.
2. Open **Analyze Email**.
3. Use a safe sample:
   - Sender: `security@example.test`
   - Subject: `URGENT account verification`
   - Body: `Your account will be suspended today. Verify your password immediately at https://secure-login.example.test/verify.`
4. Click **Analyze Email**.
5. Explain the score:
   - urgency
   - credential language
   - security-themed URL
   - HTTPS/URL properties
6. Open **Dashboard** and show the stored analysis.
7. Add a safe legitimate sample and compare the scores.
8. Open **Awareness Center** and explain the recommended response.
9. Mention that URLs are never opened and credentials are never collected.
