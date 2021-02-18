from app import db
from app import app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20))
    date_joined = db.Column(db.String(20))

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    learning = db.Column(db.Integer)
    questions = db.Column(db.Integer)
    referrals = db.Column(db.Integer)
    total = db.Column(db.Integer)
    user_id = db.Column(db.Integer)