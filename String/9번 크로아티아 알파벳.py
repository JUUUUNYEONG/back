a=input()
ct=["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt=0
for i in range(len(ct)):
    cnt+=a.count(ct[i])
    if a.count(ct[i]) >= 1:
        a=a.split(ct[i])
        a=" ".join(a)

b="".join(a.split())
cnt+=len(list(b))
print(cnt)

######다른분 코드
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
# for i in croatia:
#     word = word.replace(i, '*')
# print(len(word))

######
# a=input()
# ct=["c=","c-","dz=","d-","lj","nj","s=","z="]
# cnt=0
# for i in range(len(ct)):
#     while ct[i] in a:
#         start_indx = a.find(ct[i])
#         if len(croatia[i]) == 2:
#             end_indx = start_indx + 2
#         else:
#             end_indx = start_indx + 3
#         a=a[:start_indx]+a[end_indx:]
#         cnt+=1
# cnt+=len(list(a))
# print(cnt)
# #처음에 i번째 크로아티아 문자가 입력값에 몇개 있는지 파악 -> count 사용
# #사용하고? count 값은 다 더해준 뒤에? split으로 count가 1이상 이었던 값들을 전부다 빼준다면??
# #count 사용 결과 count가 1 이상인 문자들은 리스트에 저장
# #리스트에 저장해준 크로아티아 문자들을 하나하나 꺼내면서 split 한다 -> 반복문 사용
#
#
#크로아티아 문자가 입력값에 어느 위치에 있는지 파악 -> find 사용
#find로 알아낸 인덱스를 리스트에 저장(이때, 크로아티아 문자가 3자리 일 경우, 또 다른 list에 저장한다)
#문자열 슬라이싱으로 크로아티아 문자를 제외한 문자열 개수 계산