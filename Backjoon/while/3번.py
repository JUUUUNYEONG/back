a=int(input())
c=a
n=0
while True:
    if a//10==0:
        a=(a%10)*10+a%10
        n+=1
    else:
        b=(a//10)+(a%10)
        a=(a%10)*10+b%10
        n+=1
    if c==a:break
print(n)