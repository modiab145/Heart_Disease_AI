import streamlit as st
from utils.ai_chat import ask_ai

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Heart Disease AI Assistant")

# تهيئة سجل المحادثة والرسائل لو مش موجودة
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- عرض آخر تنبؤ والتوصيات لو موجود في الـ session_state ---
if "last_prediction" in st.session_state:
    pred_data = st.session_state["last_prediction"]
    raw_pred = pred_data.get('prediction')
    
    # تحديد النص والتوصيات بناءً على النتيجة (Low vs High)
    if raw_pred == 0 or raw_pred == "0":
        pred_text = "🟢 Low Risk (Healthy)"
        recommendations = [
            "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
            "Engage in regular physical activity (at least 30 minutes a day, 5 days a week).",
            "Keep monitoring your blood pressure and cholesterol levels annually.",
            "Avoid smoking and limit alcohol intake."
        ]
        suggested_questions = [
            "How can I maintain this low risk?",
            "What are the best foods for heart health?",
            "How often should I check my heart rate and blood pressure?"
        ]
    elif raw_pred == 1 or raw_pred == "1":
        pred_text = "🔴 High Risk (Needs Attention)"
        recommendations = [
            "Consult a cardiologist as soon as possible for a professional medical evaluation.",
            "Strictly monitor your blood pressure and blood sugar levels daily.",
            "Adopt a heart-healthy diet low in sodium, trans fats, and added sugars.",
            "Avoid strenuous physical activities until cleared by your physician."
        ]
        suggested_questions = [
            "Why did the model classify me as high risk?",
            "What are the immediate steps I should take?",
            "What lifestyle changes are critical for my condition?"
        ]
    else:
        pred_text = str(raw_pred)
        recommendations = ["Follow general healthy lifestyle guidelines."]
        suggested_questions = ["What does my prediction result mean?", "How can I improve my heart health?"]

    with st.expander("📊 View Your Latest Prediction Results & Recommendations", expanded=True):
        st.write(f"**Prediction Result:** {pred_text}")
        if "probability" in pred_data:
            st.write(f"**Probability:** {pred_data.get('probability')}")
        
        st.markdown("---")
        st.markdown("### 💡 Personalized Recommendations:")
        for rec in recommendations:
            st.markdown(f"- {rec}")
            
    # --- أزرار الأسئلة المقترحة ---
    st.markdown("#### 💬 Quick Suggested Questions:")
    cols = st.columns(len(suggested_questions))
    for i, q in enumerate(suggested_questions):
        with cols[i]:
            if st.button(q, key=f"sugg_btn_{i}"):
                # لما يضغط على الزر، بنحط السؤال في الـ prompt تلقائياً
                st.session_state.messages.append({"role": "user", "content": q})
                with st.spinner("Thinking..."):
                    answer = ask_ai(q)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                st.rerun()

else:
    st.info("💡 Tip: Make a prediction in the 'Prediction' page first so the assistant can analyze your results and give you personalized recommendations.")
    suggested_questions = [
        "What are the main risk factors for heart disease?",
        "How can I keep my heart healthy?",
        "What symptoms should I watch out for?"
    ]

st.write("---")
st.write("Ask any question about heart disease or your prediction:")

# عرض تاريخ المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال إدخال المستخدم الطبيعي من الـ chat input
prompt = st.chat_input("Ask your question...")

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        answer = ask_ai(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)