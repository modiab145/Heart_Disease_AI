import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "best_model.joblib")
DATA_PATH = os.path.join(BASE_DIR, "heart_disease_risk_2026.csv")