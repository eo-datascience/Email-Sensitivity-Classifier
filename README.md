# 🔐 Email Sensitivity Classifier

An NLP-powered application that detects whether an email contains sensitive or confidential information using machine learning. The system is built with Apache Spark, deployed via MLflow on Databricks, and served through a real-time API with a Streamlit frontend.

---

## 🚀 Project Overview

Organizations handle large volumes of email communication daily, many of which may contain sensitive information such as passwords, financial data, or confidential documents.

This project builds an end-to-end machine learning system that:

- Analyzes email content
- Detects sensitive information
- Provides real-time predictions via an API
- Displays results through an interactive web interface

---

## 🧠 Model Pipeline

The model follows a standard NLP pipeline:

1. Text preprocessing (lowercasing, tokenization)
2. Stopword removal
3. Feature extraction using TF-IDF
4. Classification using Logistic Regression

---

## 🛠️ Tech Stack

- Python  
- Apache Spark (PySpark)  
- MLflow  
- Databricks  
- Streamlit  
- Scikit-learn concepts (TF-IDF, Logistic Regression)

---
## 🌐 Deployment

- Model trained and logged using MLflow  
- Model registered in Databricks Model Registry  
- Deployed via Databricks Model Serving Endpoint  
- Streamlit app sends real-time requests to the endpoint  

---

## 💻 Streamlit App Features

- Interactive UI for email input  
- Real-time prediction  
- Clear classification output:
  - 🚨 Sensitive Email Detected  
  - ✅ Email Appears Safe  
- Clean and user-friendly design  

---

## 📊 Example Predictions

| Email Content | Prediction |
|------|--------|
| "Please send the confidential password immediately" | Sensitive |
| "Let's schedule a meeting for tomorrow" | Not Sensitive |

---

## 📷 Screenshots

_Add screenshots here_

- App Interface  
- Prediction Results  
- Databricks Endpoint  
- Model Output / Visualizations  

---

## 🔐 Security Note

For security reasons, the Databricks access token and endpoint URL are not included in this repository.  
Users should generate their own credentials and update the application accordingly.

---

## 📌 How to Run Locally

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt