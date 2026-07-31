import joblib
import pandas as pd
import streamlit as st
import os
from utils.feature_engineering import create_features

# المسار ده بيتحسب دايمًا صح مهما كان مكان تشغيل streamlit
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ده معناه: طلع من utils/ لفولدر Heart_Disease_AI، وادخل model/

@st.cache_resource
def load_model():
    model_path = os.path.join(BASE_DIR, "model", "best_model.joblib")
    model = joblib.load(model_path)
    return model

def predict_patient(patient_data: dict):
    """
    Receive patient data as a dictionary
    Return prediction and probabilities
    """

    # تحويل البيانات إلى DataFrame
    patient_df = pd.DataFrame([patient_data])

    # إنشاء الـ Features المشتقة
    patient_df = create_features(patient_df)

    # تحميل الـ Pipeline
    model = load_model()

    # Prediction
    prediction = model.predict(patient_df)[0]

    # Probability
    probability = model.predict_proba(patient_df)[0]

    return {
    "prediction": prediction,
    "probability": probability
}


