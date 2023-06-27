import sys
N=int(sys.stdin.readline())
lst=[]
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    lst.append([y,x])
for i in sorted(lst):
    print(i[1],i[0])