N=int(input())
myList=[]
for i in range(N//3+1):
    if (N-3*i)%5 == 0:
        sum=i+(N-3*i)/5
        myList.append(sum)
if len(myList) > 0:
    print(int(min(myList)))
else:
    print(-1)