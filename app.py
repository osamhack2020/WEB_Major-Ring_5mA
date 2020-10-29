from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from api import crawl_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///major-ring.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    major = db.Column(db.String(120), unique=True, nullable=False)


class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)


db.create_all()

#crawl_data.craw_wevity(Contest, db)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/sign-in')
def sign_in():
    user_list = User.query.all()
    return render_template("sign_in.html", user_list=user_list)


@app.route('/create', methods=["POST"])
def create_user():
    # 유저 생성 시
    new_user = User(name=request.form['name'], major=request.form['major'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('sign_in'))


@app.route('/all')
def show_all():
    return render_template("all.html")

@app.route('/contest')
def show_contest():
    contest_list = Contest.query.all()
    return render_template("contest.html", contest_list=contest_list)


if __name__ == '__main__':
    app.run(debug=True)
