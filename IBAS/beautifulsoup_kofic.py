import webcrawling
import requests
import json

data=kofic.Kofic("cf8fde0c0bdee60edd2f4964d21f7de8")
daily_box=data.get_daily_box_office("20221025","5")

movie_list=list()
for i in range(5):
    movieCd=daily_box["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieCd"]
    info=data.get_movie_info(movieCd)

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

    #연령제한
    movie_info["limited_age"] = info["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]

    movie_list.append(movie_info)

movie_list_title=list()
for i in range(5):
    movie_list_title.append(movie_list[i]["title"])

# 영화 제목 리스트 movie_list_title



def user():
    while(True):
        print("================\n상영중인 영화 정보\n=================\n")
        print(movie_list)
        print("=========================\n")


        input_title=input("예매하실 영화의 이름을 입력하세요. ")

        if input_title=="exit":
            print("프로그램을 종료합니다.")
            break
        if not input_title in movie_list_title:
            print("목록에 없는 영화입니다. 다시 입력해주세요.")
            continue

        input_age = input("모든 관람자의 나이를 입력하여 주시기 바랍니다. 띄어쓰기로 구분하십시오. ").split() #입력받은 나이를 리스트화
        if input_age == "exit":
            print("프로그램을 종료합니다.")
            break

        print("===========================\n")

        n = movie_list_title.index(input_title) #입력받은 영화 제목에 해당하는 딕셔너리 번호 호출
        AGE=movie_list[n]['limited_age'] #n번째 딕셔너리에 해당하는 나이
        if AGE == "12세이상관람가":
            age=12
        elif AGE == "15세이상관람가":
            age=15
        elif AGE == "청소년관람불가":
            age=20
        else: age=0


        ex_age=[] #제외된 나이 리스트
        if age:
            for i in input_age:
                if age >= int(i):
                    print("본 영화는 {0}세 이상이 관람할 수 있습니다. {1}세인 인원을 제외합니다.\n".format(age,i))
                    ex_age.append(str(i))

        input_age = [x for x in input_age if x not in ex_age] #입력 받은 나이 리스트 - 제외된 나이 리스트

        if not input_age: #모두 제외되었다면 처음 화면으로 돌아감
            print("연령 제한으로 영화를 예매할 수 없습니다.")
            continue

        type_of_age = [] #나이에 따른 연령대 구분
        for i in input_age:
            if int(i)>=65:type_of_age.append("경로")
            elif int(i)>=20:type_of_age.append("성인")
            else:type_of_age.append("아동")

        print("========\n안내\n=========") #나이 확인 끝

        #나이에 따른 금액 차이를 적용한 총 금액 출력
        print("총 {0}명 이며, 결제금액은 ,{1}원 입니다.".format(len(input_age),8000 * type_of_age.count("경로") + 10000*type_of_age.count("성인")+5000*type_of_age.count("아동")))
        answer=input("예매하시겠습니까? 예매를 하시려면 'Y' 또는 'y'를 입력하십시오.")
        if answer == 'Y' or answer == 'y':
            #출력할 영수증 딕셔너리 형성
            bill_dict=dict()
            bill_dict['경로']=str(type_of_age.count("경로")) + "명"
            bill_dict['금액']=str(8000 * type_of_age.count("경로") + 10000*type_of_age.count("성인")+5000*type_of_age.count("아동")) + "원"
            bill_dict['성인']=str(type_of_age.count("성인")) + "명"
            bill_dict['아동']=str(type_of_age.count("아동")) + "명"
            bill_dict['영화명']=input_title
            bill_dict['총원']=str(len(input_age))+"명"
            print(bill_dict)
        elif answer == "exit":
            print("프로그램을 종료합니다.")
            break
        else:
            print("취소되었습니다. 처음부터 다시 시도하여주십시오")
            continue

def admin():
    while(True):
        print("===============================\n=========저장된 영화 정보=========\n===============================")
        print(movie_list)
        print("==============================")
        ad_input=input("입력을 원하시면 '입력'을 입력하세요 :")

        if ad_input == "입력":
            data_input=input("영화명, 상영시간, 시작시간, 관람제한연령, 영화장르 순으로 띄어쓰기로 구분하여 데이터를 입력하십시오.").split()

            #필요한 정보를 모두 입력하지 않았을때 처음으로 돌려보냄
            if len(data_input) != 5:
                print("입력 형식에 맞지 않습니다. 처음으로 돌아갑니다.")
                continue

            #새로운 영화 정보를 입력할 딕셔너리를 생성, 순서에 맞게 입력
            new_dic=dict()
            new_dic['genre']=data_input.pop()
            new_dic['limited_age'] = data_input.pop()
            new_dic['start_time'] = data_input.pop()
            new_dic['running_time'] = data_input.pop()
            new_dic['title'] = data_input.pop()
            movie_list.append(new_dic)

            print("==========================")
            print("===============안내==========")
            print("==========================")
            print("영화 {0}(이)가 등록되었습니다.".format(new_dic['title']))
            print("==========================")
        elif ad_input=="exit":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바르지 않는 형식 입니다. 다시 입력하세요")

if __name__=="__main__":
    import sys
    user()