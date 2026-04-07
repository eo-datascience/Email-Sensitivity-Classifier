import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Email Sensitivity Classifier",
    page_icon="📧",
    layout="centered"
)

# Config
url = "ENDPOINT_URL"
token = "DATABRICKS_TOKEN"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Simple styling
st.markdown("""
    <style>
        .main {
            padding-top: 1.5rem;
        }
        .hero-box {
            padding: 1.2rem 1.4rem;
            border-radius: 16px;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
            margin-bottom: 1rem;
        }
        .hero-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.35rem;
        }
        .hero-subtitle {
            font-size: 1rem;
            opacity: 0.9;
        }
        .section-card {
            padding: 1rem 1.1rem;
            border-radius: 14px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            margin-top: 0.8rem;
            margin-bottom: 0.8rem;
        }
        .result-box {
            padding: 1rem 1.1rem;
            border-radius: 14px;
            margin-top: 1rem;
            font-weight: 600;
            font-size: 1.05rem;
        }
        .safe-box {
            background: #ecfdf5;
            border: 1px solid #10b981;
            color: #065f46;
        }
        .sensitive-box {
            background: #fef2f2;
            border: 1px solid #ef4444;
            color: #991b1b;
        }
        .footer-note {
            font-size: 0.9rem;
            color: #64748b;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="hero-box">
        <div class="hero-title">📧 Email Sensitivity Classifier</div>
        <div class="hero-subtitle">
            Detect potentially sensitive email content using a deployed machine learning model.
        </div>
    </div>
""", unsafe_allow_html=True)

# Sample examples   
with st.expander("Try sample emails"):
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sensitive example"):
            st.session_state["email_text"] = (
                "Please send the confidential salary spreadsheet and the admin password immediately."
            )

    with col2:
        if st.button("Safe example"):
            st.session_state["email_text"] = (
                "The event has beeen rescheduled till next week due to some delays from the organisation delivering the speech."
            )

# Input area
st.markdown('<div class="section-card">', unsafe_allow_html=True)
email_text = st.text_area(
    "Paste email content",
    height=220,
    placeholder="Enter or paste the email text here...",
    key="email_text"
)
st.markdown('</div>', unsafe_allow_html=True)

# Action buttons
def clear_text():
    st.session_state.email_text = ""

col1, col2 = st.columns([1, 1])

analyze = col1.button("Analyze Email", use_container_width=True)
col2.button("Clear", use_container_width=True, on_click=clear_text)

# Prediction section
if analyze:
    if not email_text.strip():
        st.warning("Please enter an email before running analysis.")
    else:
        data = {
            "dataframe_records": [
                {"body_lower": email_text.lower()}
            ]
        }

        with st.spinner("Analyzing email..."):
            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=60
            )
        result = response.json()

        if "predictions" not in result:
            st.error(f"Unexpected API response: {result}")
            st.stop()

        prediction = result["predictions"][0]

        st.markdown("### Prediction Result")

        if prediction == 1:
            st.markdown("""
                <div class="result-box sensitive-box">
                    🚨 Sensitive Email Detected
                </div>
            """, unsafe_allow_html=True)
            st.caption("The model flagged this email as containing potentially sensitive information.")
        else:
            st.markdown("""
                <div class="result-box safe-box">
                    ✅ Email Appears Safe
                </div>
            """, unsafe_allow_html=True)
            st.caption("The model did not detect strong sensitivity signals in this email.")


# Footer
#st.markdown("""
#    <div class="footer-note">
#        This app sends the email text to a deployed Databricks model serving endpoint for real-time inference.
#    </div>
#""", unsafe_allow_html=True)