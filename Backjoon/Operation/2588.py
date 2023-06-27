a=int(input())
b=input()
n=0
for i in range(3):
    n+=a*int(b[2-i])*10**i
    print(a*int(b[2-i]))
print(n)