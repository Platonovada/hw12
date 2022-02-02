import json


def settings():  # возвращает список настроек
    with open('settings.json','r') as f:
        data = json.load(f)
    return data


def get_candidates():  # возвращает список кандидатов
    with open('candidates.json','r') as f:
        candidate = json.load(f)
    return candidate


def get_candidate_cid(cid):  # поиск кандидата по id
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == cid:
            return candidate


def search_candidates(name):  # поиск по имени
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


def search_in_skills(skill):  # поиск по навыку
    get_setting = settings()
    get_setting = get_setting["limit"]
    candidates = get_candidates()
    names = []
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower():
            names.append(candidate)
    if len(names) > get_setting:
        while len(names) != get_setting:
            names.pop()
            return names
    else:
        return names

print(get_candidate_cid(1))