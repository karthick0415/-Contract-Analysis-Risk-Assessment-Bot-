import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Model that EXISTS for your key (you proved this)
model = genai.GenerativeModel("gemini-flash-latest")

def explain_clause(clause):
    prompt = f"""
You are a legal assistant for Indian small businesses.

Explain the following contract clause in VERY SIMPLE business English.

1. What this clause means
2. What risk it creates for a small business
3. One safer alternative or negotiation suggestion

Rules:
- No legal jargon
- No law names
- Simple English only

Clause:
{clause}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        # ✅ Fallback ONLY if AI is unavailable
        return (
            "⚠ AI explanation temporarily unavailable.\n\n"
            "Simple explanation:\n"
            "- This clause creates financial risk for your business.\n"
            "- It may expose you to high or unlimited losses.\n"
            "- You should negotiate limits or mutual protection."
        )
