import sys
N=sys.stdin.readline().rstrip()
lst = list(map(int,"_".join(N).split("_")))
for i in range(len(N)-1,-1,-1):
    print(sorted(lst)[i],end="")