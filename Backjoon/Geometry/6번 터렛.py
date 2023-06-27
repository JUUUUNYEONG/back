import math
import sys
N=int(input())
for i in range(N):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    D=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if D==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif D==(r1+r2):
        print(1)

    elif D>(r1+r2):
        print(0)
    elif D<(r1+r2):
        if D==abs(r1-r2):
            print(1)
        elif D<abs(r1-r2):
            print(0)
        else:
            print(2)

