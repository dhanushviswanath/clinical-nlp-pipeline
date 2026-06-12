from .preprocessing import clean_text
from .entity_extraction import extract_entities
from .sectionizer import split_sections
from .context import detect_negation
from .postprocessing import format_output

def run_pipeline(text: str) -> dict:
    cleaned = clean_text(text)
    sections = split_sections(cleaned)
    entities = extract_entities(cleaned)
    negation_found = detect_negation(cleaned)

    result = {
        "text": cleaned,
        "sections": sections,
        "entities": entities,
        "negation_found": negation_found,
        "entity_count": len(entities),
    }
    return format_output(result)
