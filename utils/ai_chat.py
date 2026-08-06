from groq import Groq
import streamlit as st
import os

# Read API Key
api_key = st.secrets.get("GROQ_API_KEY")

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

# Stop if API Key is missing
if not api_key:
    st.error("❌ GROQ_API_KEY not found.")
    st.stop()

# Create Groq Client
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize Groq client: {e}")
    st.stop()


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
    last_pred = st.session_state.get("last_prediction")

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    if last_pred:
        messages.append(
            {
                "role": "system",
                "content": f"Patient prediction data: {last_pred}"
            }
        )

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.4,
            max_tokens=300
        )

        return completion.choices[0].message.content

    except Exception as e:
        st.error(f"Groq Error: {e}")
        return "⚠️ Unable to contact the AI service. Please try again later."
