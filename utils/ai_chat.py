from groq import Groq
import streamlit as st
import os

# Read API Key (Streamlit Cloud first, then local environment)
api_key = st.secrets.get("GROQ_API_KEY", None)

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

# Stop app if no API key is found
if not api_key:
    st.error(
        "❌ GROQ_API_KEY not found. Please add it to Streamlit Secrets."
    )
    st.stop()

# Create Groq client
client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are an expert medical AI assistant specialized in cardiovascular diseases.

You answer questions about:
- Heart Disease
- Blood Pressure
- Cholesterol
- Diabetes
- BMI
- Exercise
- Smoking
- Healthy Lifestyle

Rules:
1. Give simple medical explanations.
2. Never diagnose diseases.
3. Always recommend consulting a physician.
4. Keep answers short (100-200 words).
5. If patient prediction data is provided, use it to personalize your explanation and help the user understand their results.
"""

def ask_ai(question):
    last_pred = st.session_state.get("last_prediction", None)

    messages_list = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    if last_pred:
        messages_list.append(
            {
                "role": "system",
                "content": f"Patient's latest prediction data and results: {last_pred}",
            }
        )

    messages_list.append(
        {
            "role": "user",
            "content": question,
        }
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages_list,
            temperature=0.4,
            max_tokens=300,
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"
