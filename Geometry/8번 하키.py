W,H,X,Y,P=map(int,input().split())
cnt=0
for _ in range(P):
    x1,y1=map(int,input().split())
    d1=(X-x1)**2+((Y+H/2)-y1)**2
    d2=((X+W)-x1)**2+((Y+H/2)-y1)**2
    if X <= x1 <= X+W and Y <= y1 <= Y+H:
        cnt+=1
        pass
    elif x1 < X and d1 <= (H/2)**2:
        cnt+=1
        pass
    elif x1 > X+W and d2 <= (H/2)**2:
        cnt+=1
        pass
print(cnt)