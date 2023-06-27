# # def first(n):
# #     print(star(n/3))
# #
# #     first(n/3)*3
# #     second(n/3)*3
# #     first(n/3)*3
# #
# #
# # def second(n):
# #     return star(n/3)
# #
# # def star(n):
# #     if n==1:
# #         return "*"
# #     else:
# #         return star(n/3)*3
#
# def middle_line(n,str):
#     if n==1:
#         return str
#     else:
#         return middle_line(n/3,str) + " "*int(n/3) + middle_line(n/3,str)
# #print(middle_line(9,"***"))
#
# def fir(str):
#         return str*3

def ah(n,str):
    if n==3:
        return str + " " * int(n / 3) + str
    else:
        return ah(n/3,str)

def star(n):
    if n==1:
        return "*"
    else:
        return star(n/3)*3 +'k'+ah(3*n,star(n/3))+'k'+star(n/3)*3

print(star(9))
print("\n".join(star(9).split("k")))

# ############################
# print(fir(3,"*"))
# print(ah(3,"*"))
# print(fir(3,"*"))
# #요 3놈을 \n으로 조인합니다
# # 1 \n 2 \n 3 이렇게 되겠죠?
# #한줄을 리턴
#
# ############################
# #리턴한 한줄을 \n으로 스플릿
# #리스트 안에 3개의 문자열이 있죠 각각 넣어줍니다
# print(fir(3,fir(3,"*")))
# print(fir(3,ah(3,"*")))
# print(fir(3,fir(3,"*")))
# #==fir(3,star(3))
#
# print(ah(9,fir(3,"*")))
# print(ah(9,ah(3,"*")))
# print(ah(9,fir(3,"*")))
# #==ah(9,star(3))
# print(fir(3,fir(3,"*")))
# print(fir(3,ah(3,"*")))
# print(fir(3,fir(3,"*")))
# #==fir(3,star(3))
# #이 모든 녀석들을 한줄로 리턴 \n으로 조인한뒤에 ->star(9)
# #############################
# fir(3,star(9))
# ah(27,star(9))