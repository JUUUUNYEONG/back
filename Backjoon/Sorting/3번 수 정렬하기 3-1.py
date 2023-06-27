import sys
N=int(sys.stdin.readline())
out_range=[0] * 10001
for _ in range(N):
    x=int(sys.stdin.readline())
    out_range[x]+=1
for i in range(10001):
    for _ in range(out_range[i]):
        print(i)
