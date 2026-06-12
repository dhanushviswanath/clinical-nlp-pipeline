import re

SECTION_HEADERS = [
    "HPI",
    "ASSESSMENT",
    "PLAN",
    "MEDICATIONS",
    "HISTORY",
    "FAMILY HISTORY",
    "SOCIAL HISTORY",
    "DISCHARGE DIAGNOSIS",
]

def split_sections(text: str) -> dict:
    if not text:
        return {"full_text": ""}
    sections = {"full_text": text}
    return sections
