import sys
N=int(sys.stdin.readline())
lst=[]
for _ in range(N):
    age,name=sys.stdin.readline().split()
    lst.append([int(age),name.rstrip()])
for i in sorted(lst,key = lambda x:x[0]):
    print(i[0],i[1])