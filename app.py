import streamlit as st
from file_loader import load_file
from nlp_engine import extract_clauses, extract_entities, obligation_type
from risk_engine import risk_score
from legal_ai import explain_clause
from audit_logger import log_audit
from langdetect import detect
from deep_translator import GoogleTranslator

st.set_page_config("Contract Analysis & Risk Assessment Bot", layout="wide")
st.title("📄 Contract Analysis & Risk Assessment Bot")

uploaded_file = st.file_uploader("Upload Contract", ["txt", "pdf", "docx"])

if uploaded_file:
    text = load_file(uploaded_file)
    lang = detect(text)

    if lang == "hi":
        text = GoogleTranslator(source="hi", target="en").translate(text)
        st.info("Hindi contract normalized to English for analysis")

    st.subheader("Contract Content")
    st.text_area("Text", text, height=200)

    clauses = extract_clauses(text)
    entities = extract_entities(text)

    total_risk = 0

    st.subheader("Clause Analysis")

    for i, clause in enumerate(clauses):
        score, level = risk_score(clause)
        total_risk += score

        with st.expander(f"Clause {i+1} | Risk: {level}"):
            st.write(clause)
            st.write("Type:", obligation_type(clause))
            st.write("Risk Score:", score)

            if level != "LOW":
                explanation = explain_clause(clause)
                st.info(explanation)

    contract_score = total_risk // max(len(clauses), 1)

    st.subheader("📊 Contract Risk Summary")
    st.metric("Overall Risk Score", contract_score)

    st.subheader("📌 Extracted Key Information")
    st.json(entities)

    log_audit({
        "risk_score": contract_score,
        "entities": entities
    })
