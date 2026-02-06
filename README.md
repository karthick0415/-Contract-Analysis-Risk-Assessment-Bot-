# 📄 Contract Analysis & Risk Assessment Bot

An AI-assisted legal contract analysis system that helps **Small and Medium Enterprises (SMEs)** understand complex contracts, identify legal risks, and receive actionable explanations in plain business language.

---

## 🚀 Project Overview

Legal contracts often contain complex clauses that are difficult for non-legal professionals to interpret. Small businesses may unknowingly agree to unfavorable terms such as unlimited liability, unilateral termination, or foreign arbitration.

This project addresses that challenge by providing an **automated contract analysis tool** that:
- Breaks contracts into clauses
- Identifies risky clauses
- Explains risks in simple English
- Suggests safer alternatives
- Computes an overall contract risk score

The system is designed with **AI + fallback reliability**, ensuring uninterrupted analysis even when AI services are unavailable.

---

## 🎯 Key Features

### 🔍 Contract Understanding
- Clause-by-clause extraction
- Clause classification (Obligation / Right / Neutral)
- Rule-based legal risk identification

### ⚠️ Risk Assessment
- Clause-level risk classification (Low / Medium / High)
- Detection of:
  - Unlimited liability
  - Indemnity clauses
  - Unilateral termination
  - Auto-renewal clauses
  - Arbitration & jurisdiction clauses

### 🤖 AI-Powered Explanation
- Plain English explanations for **high-risk clauses**
- Simple business language (no legal jargon)
- Negotiation suggestions & safer alternative wording

### 🔁 Fallback Mechanism
- Rule-based explanation when AI is unavailable
- Ensures reliability, demo safety, and cost control

### 📌 Information Extraction
- Parties involved
- Dates & durations
- Financial terms (if present)

### 📊 Risk Summary
- Composite contract risk score
- Visual risk indicators for quick decision-making

### 🔐 Audit & Traceability
- User actions logged
- Analysis stored in JSON audit logs

---

## 🧠 Technology Stack

| Component | Technology |
|---------|------------|
| Language | Python |
| UI | Streamlit |
| NLP | Rule-based NLP, spaCy (extendable) |
| AI Model | Google Gemini (LLM-agnostic design) |
| Storage | JSON (audit logs) |
| Deployment | Streamlit Community Cloud |

---

## 🏗️ System Architecture

The system follows a modular layered architecture:
- Presentation Layer – Streamlit UI
- Processing Layer – File loader & NLP engine
- Risk Layer – Rule-based risk engine
- Intelligence Layer – AI explanation module with fallback
- Audit Layer – JSON-based audit logging
- Output Layer – Risk summary and insights

---

## 📂 Project Structure

```
genai_legal_assistant/
│
├── app.py
├── file_loader.py
├── nlp_engine.py
├── risk_engine.py
├── legal_ai.py
├── audit_logger.py
├── audit_log.json
├── sample_high_risk.txt
├── sample_low_risk.txt
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

(Optional) Set API key:
```bash
setx GEMINI_API_KEY "your_api_key_here"
```

---

## ⚠️ Disclaimer

This tool is for **educational purposes only** and does not constitute legal advice.

---

## 👨‍💻 Author

**Karthick S**  
B.E. Computer Science and Engineering  
Final Year Project  
