#api for crawling
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def crawl_wevity(Contest, db):
    for i in range(0, 99):
        url = "https://www.wevity.com/?c=find&s=1&gp=" + str(i)
        soup = BeautifulSoup(urlopen(url), "html.parser")
        # 불필요 span 태그 제거
        for span in soup.select('div.ms-list a > span'):
            span.replaceWith('')
        contest_list = soup.select('ul.list li')
        for contest in contest_list[1:]:
            contest_title           = str(contest.find('div', {'class': 'tit'}).find('a').get_text().strip())
            contest_category        = str(contest.find('div', {'class': 'sub-tit'}).get_text()[5:])
            contest_organization    = str(contest.find('div', {'class': 'organ'}).get_text().strip())
            # print("제목: " + contest_title)
            # print("카테고리 :" + str(contest_category))
            # print("주최사: " + contest_organization)
            new_contest = Contest(title=contest_title, category=contest_category, organization=contest_organization)
            db.session.add(new_contest)
            db.session.commit()