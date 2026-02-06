import os

model = None
import os

API_KEY = os.getenv("GEMINI_API_KEY")
print("DEBUG → GEMINI_API_KEY FOUND:", bool(API_KEY))


try:
    import google.generativeai as genai

    API_KEY = os.getenv("GEMINI_API_KEY")

    if API_KEY:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-flash-latest")

except Exception:
    model = None


def explain_clause(clause):
    # If API key or model is not available → fallback
    if model is None:
        return (
            "⚠ AI explanation unavailable (API key not configured).\n\n"
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

