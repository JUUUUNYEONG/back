a,b=map(int,input().split())
table=[True] * (b+1)
result=[]
for i in range(2,b+1):
    if table[i]:
        if a <= i:
            print(i)
        for j in range(i*2,b+1,i):
            table[j]=False
