a=int(input())
c=0
for i in range(a):
    cnt = 0
    b=input()
    s1=set(b)
    for j in s1:
        k = b.count(j)
        if j*k in b:
            cnt+=1
    if cnt == len(s1):
        c+=1
print(c)
#연속된 단어로만 구성되어야 한다
#같은 알파벳 끼리는 떨어져않아야 한다
#1. count 함수를 사용해서 문자열에 존재하는 알파벳의 개수를 파악
#2. count로 나온 개수만큼 문자열을 반복해서 문자뎔에 존재하는 지 확인
#3. True가 나오면 cnt 1 증가


# n = int(input())
# cnt = n
#
# for i in range(n):
#     word = input()
#     for j in range(0, len(word) - 1):
#         if word[j] == word[j + 1]:
#             continue
#         elif word[j] in word[j + 1:]: #이후의 문자열에서 문자 존재 여부 확인
#             cnt -= 1
#             break
#
# print(cnt)