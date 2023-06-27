import sys
N=int(sys.stdin.readline())
lst=[]
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    lst.append([x,y])

for i in sorted(lst):
    print(i[0],i[1])