T=int(input())
l1=[]
l2=[]
for i in range(1,T+1):
    a,b=map(l1.append,input().split())
    l2.append(l1)
    l1=[]
for i in range(T):
    print(int(l2[i][0])+int(l2[i][1]))