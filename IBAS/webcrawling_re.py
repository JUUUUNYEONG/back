import webcrawling
import requests
import json

data=kofic.Kofic("cf8fde0c0bdee60edd2f4964d21f7de8")
daily_box=data.get_daily_box_office("20221025","5")
movie_dict=dict()

movieCd = daily_box["boxOfficeResult"]["dailyBoxOfficeList"][0]["movieCd"]
info = data.get_movie_info(movieCd)
print(json.dumps(info,indent=4,ensure_ascii=False))

for i in range(5):
    movieCd=daily_box["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieCd"]
    info=data.get_movie_info(movieCd)

    ##출력
    print(json.dumps(info,indent=4,ensure_ascii=False))

    #영화제목 EN
    movie_info=dict()
    movie_info['titleEn']=info["movieInfoResult"]["movieInfo"]["movieNmEn"]

    #영화제목
    movie_info['title']=info["movieInfoResult"]["movieInfo"]["movieNm"]

    #배우
    actors_list=list()
    for j in range(0, 5 if len(info["movieInfoResult"]["movieInfo"]["actors"])>=5 else len(info["movieInfoResult"]["movieInfo"]["actors"])):
        actors_list.append(info["movieInfoResult"]["movieInfo"]["actors"][j]["peopleNm"])

    movie_info['actors']=actors_list

    #감독
    movie_info['directors']=info["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"]

    #장르
    genres_list=list()
    for l in range(len(info["movieInfoResult"]["movieInfo"]["genres"])):
        genres_list.append(info["movieInfoResult"]["movieInfo"]["genres"][l]["genreNm"])
    movie_info['genres']=genres_list

    #국가명
    movie_info['nations']=(info["movieInfoResult"]["movieInfo"]["nations"][0]["nationNm"])

    #러닝타임
    movie_info['runningtime']=info["movieInfoResult"]["movieInfo"]["showTm"]
    movie_dict["movie_"+str(i)]=movie_info

    #연령제한
    movie_info["limited_age"]=info["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]
print(movie_dict)

