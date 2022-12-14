from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index():
    """

    :return: Возвращаем список кандидатов
    """
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidates_by_pk(pk)
    if not candidate:
        return 'Не найдено'
    return render_template('candidate.html', candidate=candidate)


@app.route("/skill/<skill>")
def get_by_skill(skill):
    candidates = utils.get_candidates_by_skills(skill)
    count = len(candidates)
    return render_template('skills.html', candidates=candidates, count=count, skill=skill)



@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    count = len(candidates)
    return render_template('search.html', candidates=candidates, count=count)


app.run(debug=True)
