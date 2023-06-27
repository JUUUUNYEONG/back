N=int(input())
for _ in range(N):
    x1,y1,x2,y2=map(int,input().split())
    T=int(input())
    cnt=0
    for j in range(T):
        c1,c2,r=map(int,input().split())
        d1 = (x1 - c1) ** 2 + (y1 - c2) ** 2
        d2 = (x2 - c1) ** 2 + (y2 - c2) ** 2
        Rd = r ** 2
        if d1 > Rd and d2 > Rd: #4가지 경우의 수 중에서 1가지를 제외
            pass
        elif d1 > Rd:
            cnt+=1
        elif d2 > Rd:
            cnt+=1
    print(cnt)