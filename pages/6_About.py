import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="About",
    page_icon="❤️",
    layout="centered"
)

# ==========================================
# Title
# ==========================================

st.title("❤️ About This Project")

st.markdown("---")

# ==========================================
# Project Description
# ==========================================

st.markdown("""
### Heart Disease Prediction System

This application is an AI-powered Heart Disease Prediction System designed to help assess the likelihood of heart disease based on patient clinical data.

The project integrates advanced **Machine Learning** techniques with an interactive **Streamlit** interface, allowing users to:

- 📊 Explore patient data through interactive dashboards.
- 🤖 Predict the risk of heart disease using trained ML models.
- 📈 Understand model predictions with explainable AI techniques.
- 💬 Interact with an AI Assistant for additional health insights.

This project was developed for educational and portfolio purposes, demonstrating an end-to-end Machine Learning workflow including data preprocessing, exploratory data analysis (EDA), model training, evaluation, explainability, and deployment.
""")

st.markdown("---")

# ==========================================
# Developers
# ==========================================

st.subheader("👨‍💻 Designed & Developed By")

st.markdown("""
- **Eng. Omar Gharib**
- **Eng. Mohamed Tamer**
- **Eng. Mohamed Ashraf**
""")

st.markdown("---")

st.caption("© 2026 Heart Disease Prediction System | All Rights Reserved")