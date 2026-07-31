from groq import Groq
import streamlit as st

from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

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
    # جلب آخر تنبؤ محفوظ من الـ session state لو موجود
    last_pred = st.session_state.get("last_prediction", None)
    
    # بناء رسالة النظام أو السياق المضاف
    messages_list = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    
    # لو فيه بيانات تنبؤ سابقة، بنضيفها كسياق للذكاء الاصطناعي
    if last_pred:
        context_message = f"Patient's latest prediction data and results: {last_pred}"
        messages_list.append({
            "role": "system",
            "content": context_message
        })
    
    # إضافة سؤال المستخدم الحالي
    messages_list.append({
        "role": "user",
        "content": question
    })

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages_list,
            temperature=0.4,
            max_tokens=300
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"