import streamlit as st

model = None

try:
    import google.generativeai as genai

    # ✅ Streamlit-native secrets access
    API_KEY = st.secrets.get("GEMINI_API_KEY")

    if API_KEY:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-flash-latest")

except Exception:
    model = None


def explain_clause(clause):
    # Fallback if AI is unavailable
    if model is None:
        return (
            "⚠ AI explanation unavailable.\n\n"
            "Simple explanation:\n"
            "- This clause creates legal or financial risk.\n"
            "- It may negatively affect a small business.\n"
            "- Consider renegotiating safer terms."
        )

    prompt = f"""
You are a legal assistant for Indian small businesses.

Explain the following contract clause in VERY SIMPLE business English.

1. What this clause means
2. What risk it creates
3. One safer alternative or negotiation suggestion

Clause:
{clause}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return (
            "⚠ AI explanation temporarily unavailable.\n\n"
            "Simple explanation:\n"
            "- This clause creates legal or financial risk.\n"
            "- It may negatively affect a small business.\n"
            "- Consider renegotiating safer terms."
        )
