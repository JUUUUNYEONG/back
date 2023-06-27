# def cal(k,n):
#     sum=0
#     if k==1:
#         sum=n*(n+1)/2
#     else:
#         for i in range(n):
#             sum+=cal(k-1,i+1)
#     return(int(sum))
# a=int(input())
# for i in range(a):
#     k=int(input())
#     n=int(input())
#     print(cal(k,n))
def combin(n):
    c=1
    for i in range(n,0,-1):
       c=c*i
    return c
a=int(input())
for i in range(a):
    k=int(input())
    n=int(input())
    print(int(combin(k+n)/(combin(k+1)*combin(n-1))))