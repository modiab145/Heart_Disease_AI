from utils.data_loader import load_dataset
import plotly.express as px
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Heart Disease Dashboard")

st.caption(
    "Interactive dashboard for exploring the heart disease dataset."
)

st.divider()

df = load_dataset()





st.sidebar.header("🔍 Filters")

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df["sex"].unique().tolist())
)

smoker = st.sidebar.selectbox(
    "Smoking Status",
    ["All"] + sorted(df["smoker_status"].unique().tolist())
)

age_group = st.sidebar.selectbox(
    "Age Group",
    ["All"] + sorted(df["age_group"].astype(str).unique().tolist())
)



filtered_df = df.copy()

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["sex"] == gender
    ]

if smoker != "All":
    filtered_df = filtered_df[
        filtered_df["smoker_status"] == smoker
    ]

if age_group != "All":
    filtered_df = filtered_df[
        filtered_df["age_group"].astype(str) == age_group
    ]




    # ==========================
# KPIs
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Patients",
        len(filtered_df)
    )

with col2:
    st.metric(
        "High Risk",
        filtered_df["has_heart_disease"].sum()
    )

with col3:
    st.metric(
        "Low Risk",
        len(filtered_df) - filtered_df["has_heart_disease"].sum()
    )

with col4:
    st.metric(
        "Average BMI",
        f"{filtered_df['bmi'].mean():.1f}"
    )

st.divider()



col_left, col_right = st.columns(2)

with col_left:

    fig_age = px.histogram(
        filtered_df,
        x="age",
        nbins=20,
        title="Age Distribution"
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )

with col_right:

    fig_target = px.pie(
        filtered_df,
        names="has_heart_disease",
        title="Heart Disease Distribution",
        hole=0.5
    )

    st.plotly_chart(
        fig_target,
        use_container_width=True
    )




    col_left, col_right = st.columns(2)

with col_left:

    fig_bmi = px.box(
        filtered_df,
        x="sex",
        y="bmi",
        color="sex",
        title="BMI Distribution by Gender"
    )

    st.plotly_chart(
        fig_bmi,
        use_container_width=True
    )

with col_right:

    fig_scatter = px.scatter(
        filtered_df,
        x="age",
        y="cholesterol_total",
        color="smoker_status",
        size="bmi",
        title="Age vs Cholesterol"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )