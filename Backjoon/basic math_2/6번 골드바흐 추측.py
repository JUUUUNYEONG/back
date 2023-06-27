T=[True]*10001
prime=[]
k=0
for j in range(2,10001):
    if T[j] == True:
        prime.append(j)
        for h in range(j * 2, 10001, j):
            T[h] = False

for i in range(int(input())):
    a=int(input())
    TT=T[:]
    pe=prime[:]
    k=0
    if TT[int(a/2)]:
        k=int(a/2)
    else:
        for j in pe:
            if j < a-j and TT[a-j]:
                k=max(k,j)
    print(k,a-k)