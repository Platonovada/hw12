import json


def settings():
    with open('settings.json','r') as f:
        data = json.load(f)
    return data


def get_candidates():
    with open('candidates.json','r') as f:
        candidate = json.load(f)
    return candidate


def get_candidate_cid(cid):
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == cid:
            return candidate