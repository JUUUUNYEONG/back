a=int(input())
b=int(input())
myList=[]
for i in range(a,b+1):

    if i==1:
        continue

    if i==2:
        myList.append(i)
        continue

    p=True

    for j in range(2,i):
        if i%j==0:
            p=False
            break
    if p:
        myList.append(i)

if len(myList)==0:
    print(-1)
else:
    print(sum(myList))
    print(min(myList))