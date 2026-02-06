import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_clauses(text):
    clauses = re.split(r'\n\n|\.', text)
    return [c.strip() for c in clauses if len(c.strip()) > 40]

def extract_entities(text):
    doc = nlp(text)
    data = {
        "PARTIES": [],
        "DATES": [],
        "AMOUNTS": [],
        "LOCATIONS": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            data["PARTIES"].append(ent.text)
        elif ent.label_ == "DATE":
            data["DATES"].append(ent.text)
        elif ent.label_ == "MONEY":
            data["AMOUNTS"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            data["LOCATIONS"].append(ent.text)

    return data

def obligation_type(clause):
    if "shall" in clause.lower():
        return "OBLIGATION"
    if "may" in clause.lower():
        return "RIGHT"
    if "shall not" in clause.lower():
        return "PROHIBITION"
    return "NEUTRAL"
