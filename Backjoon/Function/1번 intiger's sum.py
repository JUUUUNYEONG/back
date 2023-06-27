#1번
def solve(a):
    cnt = sum(i for i in a)
    return cnt

#2번
s1=set(range(10000))
s2=set()
for i in range(10000):
    ck = i + sum(int(j) for j in str(i))
    s2.add(ck)

mylist=sorted(list(s1-s2))
for i in mylist:
     print(i)

#3번
a=int(input())
cnt=0
for i in range(1,a+1):
    L=str(i)
    if len(L) <= 2:
        cnt+=1
    elif int(L[1])*2 == (int(L[0]) + int(L[2])):
        cnt+=1
print(cnt)
