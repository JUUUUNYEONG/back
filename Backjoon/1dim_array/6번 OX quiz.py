a=int(input())
b=[input().split("X") for i in range(a)]
for i in b:
    sum=0
    for j in i:
        k=int(len(j))
        sum+=k*(k+1)//2
    print(sum)

# n=int(input())
# for i in range(n):
#     T=list(filter(None, input().split('X')))
#     T1=list(len(j) for j in T)
#     S=sum(list(k*(k+1)//2 for k in T1))
#     print(S)