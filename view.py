from apps import settings, get_candidate_cid, get_candidates, search_candidates, search_in_skills

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')  # страница со статусом вкл/выкл
def page_index():
    setting = settings()
    status = setting.get("online", False)
    if status is True:
        return "Приложение работает"
    else:
        return "Приложение не работает"


@app.route('/candidate/<int:cid>')  # портфолио кандидата
def page_candidate(cid):
    candidate = get_candidate_cid(cid)
    return render_template('candidate.html', candidate=candidate)


@app.route('/list')  # список кандидатов
def page_list():
    candidates = get_candidates()
    page = "<h1> Все кандидаты </h1>"
    for candidate in candidates:
        page = page + f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return page


@app.route('/search')  # поиск по имени
def page_search():
    name = request.args.get("name", "")
    candidates = search_candidates(name)
    count_candidate = len(candidates)
    page = f"<h1>Найдено кандидатов {count_candidate}</h1>"

    for candidate in candidates:
        page = page + f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return page


@app.route('/skill/<skill>')  # поиск по навыку
def page_skill(skill):
    candidates = search_in_skills(skill)
    count_candidate = len(candidates)
    page = f"<h1>Найдено кандидатов {count_candidate}</h1>"
    for candidate in candidates:
        page = page + f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return page
