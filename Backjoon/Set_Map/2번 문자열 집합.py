import sys
N,M=map(int,sys.stdin.readline().split())
st=set()
cnt=0
for i in range(N+M):
    if len(st) < N: st.add(sys.stdin.readline().rstrip())
    else: cnt+=int(sys.stdin.readline().rstrip() in st)
print(cnt)