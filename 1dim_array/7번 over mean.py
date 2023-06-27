a=int(input())
b=[list(map(int,input().split())) for i in range(a)]
for j in range(a):
    N=b[j][0]
    mean=sum(b[j][1:])/N
    ratio=sum(i > mean for i in b[j][1:]) / N * 100
    print("%0.3f%%"%ratio)


