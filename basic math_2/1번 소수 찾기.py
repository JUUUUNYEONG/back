a=int(input())
nlist=input().split()
cnt = 0
for i in nlist:
    sum = 0
    if int(i)==2:
        cnt+=1
        continue
    #prime = True
    for j in range(2,int(i)):
        if int(i)%j==0: break #prime = False
        sum+=1
        if sum==int(i)-2: #if prime:
            cnt+=1
print(cnt)


