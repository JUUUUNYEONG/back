N=int(input())
for i in range(2,N+1):
    while N%i==0:
        N=N/i
        print(i)

# table=[True] * (N+1)
# result=[]
# for i in range(2,N+1):
#     if table[i]:
#         result.append(i)
#         for j in range(i*2,N+1,i):
#             table[j]=False
# for i in result:
#     while N%i==0:
#         N=N/i
#         print(i)