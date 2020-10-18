# public api
from flask import Flask, render_template
# api for database
from sqlalchemy import create_engine
# custom api
# import crawl_data

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
