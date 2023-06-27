a,b,c=map(int,input().split())
k=sorted("{0}{1}{2}".format(a,b,c))
if a==b==c:
    print(10000+a*1000)
elif a!=b!=c!=a:
    print(int(k[2])*100)
else:
    print(1000+int(k[1])*100)