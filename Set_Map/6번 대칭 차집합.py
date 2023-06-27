import sys
N,M=map(int, sys.stdin.readline().split())
set1=set(sys.stdin.readline().rstrip().split())
set2=set(sys.stdin.readline().rstrip().split())
print(len(set1-set2)+len(set2-set1))

