#api for crawling
from urllib.request import urlopen
from bs4 import BeautifulSoup

def craw_wevity(Contest, db):
    url = "https://wevity.com"
    soup = BeautifulSoup(urlopen(url),"html.parser")
    selects = soup.select('div',{'class':'tit'} )
    print(str(selects))
    for select in selects:
        print(str(select))
        print("##############################################3")
        new_contest = Contest(name=str(select))
        db.session.add(new_contest)
        db.session.commit()

