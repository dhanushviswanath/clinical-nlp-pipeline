from typing import List, Dict

import medspacy
from medspacy.ner import TargetRule

_nlp = medspacy.load()

target_matcher = _nlp.get_pipe("medspacy_target_matcher") if "medspacy_target_matcher" in _nlp.pipe_names else None

if target_matcher is not None and not target_matcher.rules:
    target_rules = [
        TargetRule("fever", "SYMPTOM"),
        TargetRule("cough", "SYMPTOM"),
        TargetRule("chest pain", "SYMPTOM"),
        TargetRule("diabetes", "DIAGNOSIS"),
        TargetRule("hypertension", "DIAGNOSIS"),
        TargetRule("aspirin", "MEDICATION"),
    ]
    target_matcher.add(target_rules)

def extract_entities(text: str) -> List[Dict]:
    doc = _nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append(
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
            }
        )
    return entities
