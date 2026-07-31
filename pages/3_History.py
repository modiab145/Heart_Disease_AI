import streamlit as st

from utils.history import load_history

st.set_page_config(

    page_title="Prediction History",

    page_icon="📜",

    layout="wide"

)

st.title("📜 Prediction History")

st.divider()

df = load_history()

st.dataframe(

    df,

    use_container_width=True

)




col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Predictions",
        len(df)
    )

with col2:
    st.metric(
        "High Risk",
        (df["Prediction"] == "High Risk").sum()
    )

with col3:
    st.metric(
        "Low Risk",
        (df["Prediction"] == "Low Risk").sum()
    )




    csv = df.to_csv(index=False).encode("utf-8")

st.download_button(

    "📥 Download History",

    csv,

    "prediction_history.csv",

    "text/csv"

)