a=list(input().lower())
alpha="abcdefghijklmnopqrstuvwxyz"
sum=0
for i in a:
    ind=alpha.find(i)
    if ind >= 15 and ind < 19:
        sum+=8
        continue
    elif ind >= 19 and ind < 22:
        sum+=9
        continue
    elif ind >=22:
        sum+=10
        continue
    c = ind//3
    sum=sum+c+3
print(sum)
#반복문을 좀 더 잘 이용했더라면...
# s = input()
# arr = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
# t = 0
# for i in range(len(s)):
#     for j in arr:
#         if s[i] in j:
#             t += arr.index(j)+3
# print(t)