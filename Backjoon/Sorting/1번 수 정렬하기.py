#2750번
N=int(input())
lst=[]
for i in range(N):
    lst.append(int(input()))
for j in sorted(lst):
    print(j)