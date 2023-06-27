a=input()
b=input()
sum=0
for i in range(int(a)):
    sum+=int(b[i])
print(sum)

#문자열은 반복가능하니까 바로 리스트로 묶어줬으면 더 좋았겠다..
#map함수(함수, iterable 객체들(문자열, 리스트, 튜플, 집합, 딕셔너리)

#print(sum(map(int,input())))