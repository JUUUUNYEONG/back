import sys
N=int(sys.stdin.readline())
lst=[]
chk=[]
for _ in range(N):
    x=sys.stdin.readline()
    lst.append([len(x.rstrip()),x.rstrip()])
for i in sorted(lst):
    if i[1] not in chk:
        print(i[1])
        chk.append(i[1])
    else: continue