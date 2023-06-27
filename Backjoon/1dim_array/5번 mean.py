a=int(input())
b=list(map(int,input().split()))
sum=0
for i in b:
    sum+=i/max(b)*100
print(sum/a)