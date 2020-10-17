from flask import Flask, render_template
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

from sqlalchemy import create_engine

app = Flask(__name__)



@app.route('/')#localhost:5000/static/index.html
def start():
    return render_template('index.html')

@app.route('/static/index.html')#localhost:5000/static/index.html
def home():
    return render_template('index.html')

@app.route('/static/single-post.html')#localhost:5000/static/single-post.html
def test():
    return render_template('single-post.html')

@app.route('/static/about-us.html')#localhost:5000/static/about-us.html
def test1():
    return render_template('about-us.html')

@app.route('/static/archive-blog.html')#localhost:5000/test2
def test2():
    return render_template('archive-blog.html')

@app.route('/static/contact.html')#localhost:5000/contact
def test3():
    return render_template('contact.html')

@app.route('/static/typography.html')#localhost:5000/typography
def test4():
    return render_template('typography.html')



@app.route('/crawl')
def crawl():
    html = urllib.request.urlopen("https://wevity.com")
    soup = BeautifulSoup(html, "html.parser")
    main_section = soup.find_all('div', 'main-section')
    return str(main_section)

if __name__ == '__main__':
    app.run(debug=True)
