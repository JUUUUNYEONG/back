s=True
while s:
    a=int(input())
    if a:
        T=[True] * (2*a+1)
        T[0]=False
        for i in range(2,2*a+1):
            if T[i] == True:
                for j in range(i*2,2*a+1,i):
                    T[j] = False
        print(sum(T[(a+1):(2*a+1)]))
    else: s=False