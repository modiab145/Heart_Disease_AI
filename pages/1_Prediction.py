from Heart_Disease_AI.utils import prediction
import streamlit as st
from utils.prediction import predict_patient
from utils.history import save_prediction
from utils.pdf_report import generate_pdf



st.set_page_config(
    page_title="Prediction",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ Heart Disease Prediction")

st.caption(
    "AI-powered system for predicting the risk of heart disease."
)

st.info(
    "Fill in the patient's information and click Predict to estimate the risk."
)

# ==========================
# بداية الـ Form
# ==========================

def personal_information():

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=40
        )

        sex = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    with col2:

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=25.0
        )

        family_history = st.selectbox(
            "Family History",
            [False, True],
            format_func=lambda x: "Yes" if x else "No"
        )

    return {

        "age": age,

        "sex": sex,

        "bmi": bmi,

        "family_history": family_history

    }

def clinical_information():

    st.subheader("❤️ Clinical Information")

    col1, col2 = st.columns(2)

    with col1:

        resting_bp_systolic = st.number_input(
            "Systolic BP",
            value=120
        )

        resting_bp_diastolic = st.number_input(
            "Diastolic BP",
            value=80
        )

        resting_heart_rate = st.number_input(
            "Resting Heart Rate",
            value=75
        )

    with col2:

        max_heart_rate_achieved = st.number_input(
            "Max Heart Rate",
            value=170
        )

        chest_pain_type = st.selectbox(
            "Chest Pain Type",
            [
                "Asymptomatic",
                "Non-Anginal Pain",
                "Atypical Angina",
                "Typical Angina"
            ]
        )

        exercise_induced_angina = st.selectbox(
            "Exercise Induced Angina",
            [False, True],
            format_func=lambda x: "Yes" if x else "No"
        )

        st_depression = st.number_input(
            "ST Depression",
            value=0.0
        )

    return {

        "resting_bp_systolic": resting_bp_systolic,

        "resting_bp_diastolic": resting_bp_diastolic,

        "resting_heart_rate": resting_heart_rate,

        "max_heart_rate_achieved": max_heart_rate_achieved,

        "chest_pain_type": chest_pain_type,

        "exercise_induced_angina": exercise_induced_angina,

        "st_depression": st_depression

    }

def laboratory_results():

    st.subheader("🩸 Laboratory Results")

    col1, col2 = st.columns(2)

    with col1:

        cholesterol_total = st.number_input(
            "Total Cholesterol (mg/dL)",
            min_value=50,
            max_value=500,
            value=180
        )

        hdl = st.number_input(
            "HDL (mg/dL)",
            min_value=10,
            max_value=150,
            value=50
        )

        ldl = st.number_input(
            "LDL (mg/dL)",
            min_value=10,
            max_value=300,
            value=100
        )

    with col2:

        triglycerides = st.number_input(
            "Triglycerides (mg/dL)",
            min_value=20,
            max_value=1000,
            value=150
        )

        fasting_blood_sugar = st.number_input(
            "Fasting Blood Sugar",
            min_value=50,
            max_value=400,
            value=95
        )

        hba1c = st.number_input(
            "HbA1c (%)",
            min_value=3.0,
            max_value=15.0,
            value=5.5
        )

    return {

        "cholesterol_total": cholesterol_total,
        "hdl": hdl,
        "ldl": ldl,
        "triglycerides": triglycerides,
        "fasting_blood_sugar": fasting_blood_sugar,
        "hba1c": hba1c

    }

def lifestyle_information():

    st.subheader("🏃 Lifestyle Information")

    col1, col2 = st.columns(2)

    with col1:

        smoker_status = st.selectbox(
            "Smoking Status",
            [
                "Never",
                "Current",
                "Former"
            ]
        )

        exercise_minutes_per_week = st.slider(
            "Exercise Minutes / Week",
            0,
            1000,
            150
        )

        alcohol_units_per_week = st.slider(
            "Alcohol Units / Week",
            0,
            50,
            2
        )

        sleep_hours = st.slider(
            "Sleep Hours",
            3.0,
            12.0,
            7.0
        )

    with col2:

        stress_score = st.slider(
            "Stress Score",
            0.0,
            10.0,
            5.0
        )

        daily_steps = st.number_input(
            "Daily Steps",
            min_value=0,
            max_value=30000,
            value=8000
        )

        diet_quality_score = st.slider(
            "Diet Quality Score",
            0.0,
            10.0,
            5.0
        )

        wearable_owner = st.radio(
            "Wearable Device",
            ["No", "Yes"],
            horizontal=True
        )

        wearable_owner = (wearable_owner == "Yes")

    return {

        "smoker_status": smoker_status,
        "exercise_minutes_per_week": exercise_minutes_per_week,
        "alcohol_units_per_week": alcohol_units_per_week,
        "sleep_hours": sleep_hours,
        "stress_score": stress_score,
        "daily_steps": daily_steps,
        "diet_quality_score": diet_quality_score,
        "wearable_owner": wearable_owner

    }

def main():

    with st.form("prediction_form"):

        patient_data = {}

        tab1, tab2, tab3, tab4 = st.tabs([
            "👤 Personal",
            "❤️ Clinical",
            "🩸 Laboratory",
            "🏃 Lifestyle"
        ])

        with tab1:
            patient_data.update(personal_information())

        with tab2:
            patient_data.update(clinical_information())

        with tab3:
            patient_data.update(laboratory_results())

        with tab4:
            patient_data.update(lifestyle_information())

        submitted = st.form_submit_button(
            "🔍 Predict Heart Disease Risk",
            use_container_width=True
        )

    # ==========================
    # Prediction
    # ==========================

    if submitted:

        result = predict_patient(patient_data)

        prediction = result["prediction"]
        probability = result["probability"]

        risk = probability[1] * 100

        if prediction == 1:
            status = "High Risk"
            patient_status = "Needs Medical Attention"
        else:
            status = "Low Risk"
            patient_status = "Healthy"

        save_prediction(
            patient_data["age"],
            patient_data["sex"],
            status,
            risk
        )
                # حفظ نتيجة التنبؤ عشان صفحة الـ AI Assistant تقدر توصلها
        st.session_state["last_prediction"] = {
            "prediction": int(prediction),
            "status": status,
            "risk_percentage": float(risk),
            "patient_status": patient_status,
            "input_data": patient_data
        }
        

        st.divider()

        st.subheader("📊 Prediction Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Prediction", status)

        with col2:
            st.metric("Probability", f"{risk:.2f}%")

        with col3:
            st.metric("Status", patient_status)

        st.progress(risk / 100)

        # ==========================
        # Generate PDF Report
        # ==========================

        pdf_file = generate_pdf(
            patient_data,
            status,
            risk
        )

        # Read PDF as bytes
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()

        # Download Button
        st.download_button(
            label="📄 Download Medical Report",
            data=pdf_bytes,
            file_name="Medical_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )
if __name__ == "__main__":
    main()