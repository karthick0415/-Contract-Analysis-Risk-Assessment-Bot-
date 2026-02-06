
import re
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None  # fallback for cloud deployment


def extract_clauses(text):
    clauses = re.split(r'\n\n|\.', text)
    return [c.strip() for c in clauses if len(c.strip()) > 40]

def extract_entities(text):
    entities = {
        "PARTIES": [],
        "DATES": [],
        "AMOUNTS": [],
        "LOCATIONS": []
    }

    if not nlp:
        return entities  # fallback (no crash)

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities["PARTIES"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["DATES"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["AMOUNTS"].append(ent.text)
        elif ent.label_ == "GPE":
            entities["LOCATIONS"].append(ent.text)

    return entities


def obligation_type(clause):
    if "shall" in clause.lower():
        return "OBLIGATION"
    if "may" in clause.lower():
        return "RIGHT"
    if "shall not" in clause.lower():
        return "PROHIBITION"
    return "NEUTRAL"


