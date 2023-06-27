import requests
from bs4 import BeautifulSoup
import re

import sqlite3


class NaverMovieCrawler:

    def __init__(self):
        self.base_url="https://movie.naver.com/movie/bi/mi/basic.naver"
        self.point_url="https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver"

    def basic_movie_data(self,id):
        url=self.base_url + "?code={}".format(str(id))
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        title_kr = soup.select_one("#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)").text
        title=soup.select_one("#content > div.article > div.mv_info_area > div.mv_info > strong").text

        genres = soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dd > p > span")[0].text
        genres = genres.split(",")
        nations=soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dd > p > span")[1].text
        nations = nations.split(",")
        time = soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dd > p > span")[2].text
        directors = soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dd > p")[1].text
        directors=directors.split(",")
        return {
            "id":id,
            "title_kr": title_kr,
            "title": title,
            "directors": [director.strip() for director in directors],
            "genres": [genre.strip() for genre in genres],
            "nation": [nation.strip() for nation in nations],
            "time": int(re.findall(r"\d+", time)[0])
        }

    def get_comments_in_point_list(self, id, page):

        comments=[]

        for i in range(1, page + 1):

            url=self.point_url + "?code={}&page={}".format(str(id),str(page))
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            li_tags = soup.select("body > div > div > div.score_result > ul > li")

            for li in li_tags:
                if li.select("div.score_reple > p > span > span"):
                    comment = li.select_one("div.score_reple > p > span > span > a")["data-src"].strip()
                else:
                    comment = li.select("div.score_reple > p > span")[-1].text.strip()

                if comment:
                    comments.append(comment)

        return comments

class MovieSQL:

    def __init__(self):
        self.conn = sqlite3.connect("sqlite.db")
        self.cur = self.conn.cursor()
        self.conn.execute("PRAGMA foreign_keys = 1;")
        self.conn.commit()

    def create_movie_table(self):
        query = "CREATE TABLE movie(id INTEGER PRIMARY KEY, title_kr TEXT, title TEXT, director TEXT, genre TEXT, nation TEXT, time INTEGER);"
        self.conn.execute(query)

    def create_comments_table(self):
        query = "CREATE TABLE comment(movie INTEGER, comment TEXT, FOREIGN KEY('movie') REFERENCES movie('id'));"
        self.conn.execute(query)

    def set_movie_data(self,movie):
        sql = f"INSERT INTO movie (id, title_kr, title, director, genre, nation, time) VALUES ('{movie['id']}', '{movie['title_kr']}','{movie['title']}','{', '.join(movie['directors'])}', '{', '.join(movie['genres'])}', '{', '.join(movie['nation'])}','{movie['time']}');"
        self.cur.execute(sql)
        self.conn.commit()

    def set_movie_comments_data(self,id,list):
        for item in list:
            sql = f"INSERT INTO comment (movie, comment) VALUES ({id}, '{item}')"
            self.cur.execute(sql)
        self.conn.commit()

    def get_movie_data(self,id):
        sql = f"SELECT * FROM movie WHERE id={id}"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def get_comments_data(self,id):
        sql=f"SELECT comment FROM comment WHERE movie={id}"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def close(self):
        self.conn.close()



sqlite = MovieSQL()
movie = NaverMovieCrawler()
sqlite.create_movie_table()
sqlite.create_comments_table()
sqlite.set_movie_data(movie.basic_movie_data(219402)) #에브리띵
sqlite.set_movie_comments_data(219402,movie.get_comments_in_point_list(219402,5))
sqlite.set_movie_data(movie.basic_movie_data(184516)) #블랙팬서
sqlite.set_movie_comments_data(184516,movie.get_comments_in_point_list(184516,5))
sqlite.set_movie_data(movie.basic_movie_data(43208)) #브이 포 벤테타
sqlite.set_movie_comments_data(43208,movie.get_comments_in_point_list(43208,5))

# for comment in sqlite.get_comments_data(219402):
#     print(comment[0])
# sqlite.close()
