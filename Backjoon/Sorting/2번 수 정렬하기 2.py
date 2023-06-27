import sys
N=int(sys.stdin.readline())
lst=[int(sys.stdin.readline()) for i in range(N)]
for i in sorted(lst):
    print(i)

