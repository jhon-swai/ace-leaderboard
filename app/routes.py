from app import app
from flask import render_template
from app.models import Score

from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/leaderboard', methods=["POST"])
def leaderboard():
    get_scores = Score.query.all()
    data =[]
    for score in get_scores:
        data.append(score.total)

    data_dict = {}
    num = 0
    for val in data:
        data_dict[num]=val
        num+=1

    return jsonify(data_dict)
    

@app.route('/leaderboard/<number>', methods=["POST"])
def leaderboard_referral():
    
    # this can be updated 
    data_dict = {"status": "updated"}

    return jsonify(data_dict)

    
