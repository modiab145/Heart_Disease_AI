import streamlit as st

st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️",
    layout="wide"
)

import streamlit as st

with st.sidebar:
    # استخدام use_container_width ليأخذ اللوجو العرض المناسب بشكل أنيق
    st.image("Heart_Disease_AI/assets/logo.PNG.jpeg", use_container_width=True)
    
    st.title("Heart Disease AI")
    
    st.markdown("---")
    
    st.success("System Ready")
    
    st.markdown("""
    ### Features
    - ❤️ Heart Disease Prediction
    - 📊 Explainable AI
    - 🤖 AI Assistant
    - 📄 PDF Report
    - 📈 Dashboard
    """)
st.title("❤️ Heart Disease Prediction System")

st.markdown("""
Welcome to the AI-powered Heart Disease Prediction System.

This application predicts the risk of heart disease using a trained Machine Learning model.

Use the sidebar to navigate between different pages.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "CatBoost")

with col2:
    st.metric("Accuracy", "95%")

with col3:
    st.metric("Status", "Ready ✅")