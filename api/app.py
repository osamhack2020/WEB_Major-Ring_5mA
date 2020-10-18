#public api
from flask import Flask, render_template
#api for database
from sqlalchemy import create_engine
#custom api
import crawl_data

app = Flask(__name__)


@app.route('/')  #
def start():
    return crawl_data.show_activity("https://wevity.com")
    # return render_template('index.html')

#메인 화면에 필요한 정보들
#1. 유저 테이블          - 아이디, 이름, 전공
#2. 대외활동, 공모전      - 정보, 공모전 정보
#3. 자격증 정보
#4. 취업 정보

if __name__ == '__main__':
    app.run(debug=True)
