import os

try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-flash-latest")
except Exception:
    genai = None
    model = None

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Model that EXISTS for your key (you proved this)
model = genai.GenerativeModel("gemini-flash-latest")

def explain_clause(clause):
    if not model:
        return (
            "⚠ AI explanation temporarily unavailable.\n\n"
            "Simple explanation:\n"
            "- This clause creates financial risk.\n"
            "- It may expose your business to high losses.\n"
            "- You should negotiate limits or safer terms."
        )

    prompt = f"""
You are a legal assistant for Indian small businesses.

Explain the following contract clause in VERY SIMPLE business English.

1. What this clause means
2. What risk it creates for a small business
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
            "- This clause creates financial risk.\n"
            "- It may expose your business to high losses.\n"
            "- You should negotiate limits or safer terms."
        )

