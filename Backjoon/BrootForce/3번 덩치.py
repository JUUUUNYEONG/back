a=int(input())
x=[list(map(int,input().split())) for i in range(a)]
for i in range(a):
    cnt=1
    for j in range(a):
        if x[i][0] < x[j][0] and x[i][1] < x[j][1]:
            cnt+=1
    print(cnt,end=" ")
