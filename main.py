
from flask import Flask, request, render_template
app = Flask(__name__)

from apps import settings, get_candidate_cid, get_candidates


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
    candidate = get_candidates()
    p>)
    list = f"""
    <h1>Все кандидаты</h1>
    <p><a href="/candidate/<x>">Имя кандидата</a></p>
    """

if __name__ == '__main__':
    app.run()
