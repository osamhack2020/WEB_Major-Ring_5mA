from flask import Flask, render_template
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

from sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/crawl')
def crawl():
    html = urllib.request.urlopen("https://wevity.com")
    soup = BeautifulSoup(html, "html.parser")
    main_section = soup.find_all('div', 'main-section')
    return str(main_section)

if __name__ == '__main__':
    app.run(debug=True)
