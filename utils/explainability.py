import shap
import joblib

model = joblib.load("best_model.joblib")


def explain_prediction(patient_df):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer(patient_df)

    return shap_values