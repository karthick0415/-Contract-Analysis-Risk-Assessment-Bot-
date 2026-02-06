def risk_score(clause):
    keywords = {
        "HIGH": ["indemnity", "penalty", "liability", "termination", "non-compete"],
        "MEDIUM": ["arbitration", "jurisdiction", "auto-renewal", "lock-in"],
    }

    clause_lower = clause.lower()

    for k in keywords["HIGH"]:
        if k in clause_lower:
            return 80, "HIGH"

    for k in keywords["MEDIUM"]:
        if k in clause_lower:
            return 50, "MEDIUM"

    return 20, "LOW"
