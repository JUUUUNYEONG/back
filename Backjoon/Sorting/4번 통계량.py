import sys
N=int(sys.stdin.readline())
lst=[0]*8001

summ=0
med=0
most=0
cnt=0

for i in range(N):
    x=int(sys.stdin.readline())
    lst[x+4000]+=1
    summ=summ+x

for i in range(len(lst)):
    med=med+lst[i]
    if med >= (N//2 + 1):
        med=i-4000
        break

for i in range(len(lst)):
    if lst[i]:
        if cnt==0:
            minn = i-4000
        cnt+=lst[i]
    if cnt == N:
        maxx = i-4000
        break

if lst.count(max(lst)) >= 2:
    lst[lst.index(max(lst))] = 0
    most = lst.index(max(lst)) - 4000
else:
    most = lst.index(max(lst)) - 4000

print(round(summ/N)) #산술평균
print(med) #중앙값
print(most) #최빈값
print(maxx-minn) #범위


