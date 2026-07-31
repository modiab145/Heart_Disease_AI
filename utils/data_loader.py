import os
import pandas as pd


def load_dataset():

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    DATA_PATH = os.path.join(
        BASE_DIR,
        "data",
        "heart_disease_risk_2026.csv"
    )

    df = pd.read_csv(DATA_PATH)

    # ======================
    # Feature Engineering
    # ======================

    age_bins = [0, 40, 55, 70, 120]

    age_labels = [
        "Young",
        "Middle_Age",
        "Senior",
        "Elderly"
    ]

    df["age_group"] = pd.cut(
        df["age"],
        bins=age_bins,
        labels=age_labels
    )

    smoking_map = {
        "Never": 0,
        "Former": 1,
        "Current": 2
    }

    df["smoker_numeric"] = df["smoker_status"].map(smoking_map)

    df["smoker_family_risk"] = (
        df["smoker_numeric"] *
        df["family_history"].astype(int)
    )

    df["pulse_pressure"] = (
        df["resting_bp_systolic"] -
        df["resting_bp_diastolic"]
    )

    df["non_hdl"] = (
        df["cholesterol_total"] -
        df["hdl"]
    )

    df["ldl_to_hdl_ratio"] = (
        df["ldl"] /
        df["hdl"]
    )

    df["total_to_hdl_ratio"] = (
        df["cholesterol_total"] /
        df["hdl"]
    )

    df["heart_rate_reserve"] = (
        df["max_heart_rate_achieved"] -
        df["resting_heart_rate"]
    )

    return df