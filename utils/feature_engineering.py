import pandas as pd


def create_features(df):

    # ==========================
    # Pulse Pressure
    # ==========================
    df["pulse_pressure"] = (
        df["resting_bp_systolic"]
        - df["resting_bp_diastolic"]
    )

    # ==========================
    # LDL / HDL Ratio
    # ==========================
    df["ldl_to_hdl_ratio"] = (
        df["ldl"] / df["hdl"]
    )

    # ==========================
    # Non HDL
    # ==========================
    df["non_hdl"] = (
        df["cholesterol_total"]
        - df["hdl"]
    )

    # ==========================
    # Total / HDL Ratio
    # ==========================
    df["total_to_hdl_ratio"] = (
        df["cholesterol_total"]
        / df["hdl"]
    )

    # ==========================
    # Heart Rate Reserve
    # ==========================
    df["heart_rate_reserve"] = (
        df["max_heart_rate_achieved"]
        - df["resting_heart_rate"]
    )

    # ==========================
    # Age Group
    # ==========================
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

    # ==========================
    # Smoker Numeric
    # ==========================
    smoking_map = {
        "Never": 0,
        "Former": 1,
        "Current": 2
    }

    df["smoker_numeric"] = (
        df["smoker_status"].map(smoking_map)
    )

    # ==========================
    # Smoker Family Risk
    # ==========================
    df["smoker_family_risk"] = (
        df["smoker_numeric"]
        * df["family_history"].astype(int)
    )

    return df