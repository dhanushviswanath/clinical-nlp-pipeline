NEGATION_TERMS = {"no", "not", "denies", "without", "negative"}

def detect_negation(text: str) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return any(term in lowered for term in NEGATION_TERMS)
