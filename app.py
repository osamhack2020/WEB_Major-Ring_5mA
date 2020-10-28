from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    major = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/sign-in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/create', methods=["POST"])
def create_user():
    new_user = User(name=request.form['name'], major=request.form['major'])
    db.session.add(new_user)
    db.session.commit()
    return render_template('database.html', query=User.query.all())


if __name__ == '__main__':
    app.run(debug=True)
