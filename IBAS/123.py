import requests
import re
from bs4 import BeautifulSoup

class NaverMovieCrawler:

    def __init__(self):
        self.basic_url="https://movie.naver.com/movie/bi/mi/basic.naver"


url="https://movie.naver.com/movie/bi/mi/basic.naver?code=120788"

response = requests.get(url)
print(response.content)

soup = BeautifulSoup(response.content,"html.parser")
print(soup.title)

title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')
print(title.text)

genre = soup.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a:nth-child(1)")
print(genre.text)