import sys
pocket_name={}
pocket_digit={}

def pocketmon(x):
    if x in pocket_name:
        return pocket_name[x]
    else:
        return pocket_digit[x]
N,M=map(int,sys.stdin.readline().split())
for i in range(1,N+1):
    x=sys.stdin.readline().rstrip()
    pocket_digit[str(i)]=x
    pocket_name[x]=str(i)

print("\n".join(map(pocketmon,list(sys.stdin.readline().rstrip() for j in range(M)))))