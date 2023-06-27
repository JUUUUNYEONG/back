import sys
N,X=map(int,sys.stdin.readline().split())
a=input().split()
n=0
for i in range(N):
    if int(a[n+i]) >= X:
        del a[n+i]
        n=n-1
print(" ".join(a))
