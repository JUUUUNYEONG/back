import sys
N,M=map(int,sys.stdin.readline().split())
hear_set={sys.stdin.readline().rstrip() for i in range(N)}
see_set={sys.stdin.readline().rstrip() for j in range(M)}
st=hear_set.intersection(see_set)
print(len(st))
for i in sorted(st):
    print(i)