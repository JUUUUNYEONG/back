n=int(input())
qq=[]
for j in range(n+1):
    if n==sum(list(map(int,str(j))))+j:
        qq.append(j)
if not qq:
    print(0)
else:
    print(min(qq))

#k=" ".join(str(j)).split()
#k.append(str(j))