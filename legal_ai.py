import os

model = None

try:
    import google.generativeai as genai
    API_KEY = os.getenv("GEMINI_API_KEY")

    if API_KEY:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-flash-latest")

except Exception:
    model = None


def explain_clause(clause):
    if model is None:
        return (
            "⚠ AI explanation unavailable (API key not configured).\n\n"
            "Simple explanation:\n"
            "- This clause creates legal or financial risk.\n"
            "- It may negatively affect a small business.\n"
            "- Consider renegotiating safer terms."
        )

    prompt = f"""
Explain the following contract clause in VERY SIMPLE business English.

1. What this clause means
2. What risk it creates
3. One safer alternative

Clause:
{clause}
"""

    try:
        return model.generate_content(prompt).text
    except Exception:
        return (
            "⚠ AI explanation temporarily unavailable.\n\n"
            "Simple explanation:\n"
            "- This clause creates legal or financial risk.\n"
            "- It may negatively affect a small business.\n"
            "- Consider renegotiating safer terms."
        )
