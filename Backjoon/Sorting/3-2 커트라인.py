import sys
N,k=map(int,sys.stdin.readline().split())
score=list(map(int,sys.stdin.readline().split()))
print(sorted(score)[N-k])