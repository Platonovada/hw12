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


def search_candidates(name):
    candidates = get_candidates()
    get_setting = settings()
    get_setting = get_setting["case-sensitive"]
    names = []
    if get_setting is True:
        for candidate in candidates:
            if name in candidate["name"]:
                names.append(candidate)
    else:
        for candidate in candidates:
            if name.lower in candidate["name"].lower():
                names.append(candidate)
    return names

def search_in_skills(skill):
    get_setting = settings()
    get_setting = get_setting["limit"]
    candidates = get_candidates()
    names = []
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower():
            names.append(candidate["name"])
    if len(names) > get_setting:
        while len(names) != get_setting:
            names.pop()
            return names
    else:
        return names


print(search_in_skills("python"))
