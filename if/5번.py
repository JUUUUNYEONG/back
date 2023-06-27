H,M=map(int,input().split())
if M<45:
    M+=60
    H-=1
    if H<0:
        H=23
print(H,M-45)

a,b=map(int,input().split())
if b<45:
    if a==0:
        print("23 {0}".format(60-(45-b)))
    else:
        print("{0} {1}".format(a-1,60 - (45-b)))
elif b==45:
    print("{0} 0".format(a))
else:
    print("{0} {1}".format(a,b))
