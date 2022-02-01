
from flask import Flask, request, render_template
app = Flask(__name__)

from apps import settings, get_candidate_cid, get_candidates, search_candidates, search_in_skills


@app.route('/')
def page_index():
    setting = settings()
    status = setting.get("online",False)
    if status is True:
        return "Приложение работает"
    else:
        return "Приложение не работает"

@app.route('/candidate/<int:cid>')
def page_candidate(cid):
    candidate = get_candidate_cid(cid)
    page = f"""
    <h1>{candidate["name"]}</h1>
    <p>{candidate["position"]}</p>
    <img src="{candidate["picture"]}" width=200/>
    <p>{candidate["skills"]}</p>
    """
    return page

@app.route('/list')
def page_list():
    candidates = get_candidates()
    list = "<h1> Все кандидаты </h1>"
    for candidate in candidates:
        list = list + f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return list

@app.route('/search')
def page_search():
    name = request.args.get("name","")
    candidates = search_candidates(name)
    count_candidate = len(candidates)
    search = f"<h1>Найдено кандидатов {count_candidate}</h1>"

    for candidate in candidates:
        search = search + f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return search

@app.route('/skill/<str:skill>')
def page_skill(skill):
    candidates = search_in_skills(skill)



if __name__ == '__main__':
    app.run()
