a,m=map(int,input().split())
k=input().split()
qq=[]
for i in range(a):
    for j in range(a):
        for l in range(a):
            if i==j or j==l or i==l:
                continue
            cnt=int(k[i]) + int(k[j]) + int(k[l])
            if cnt <= m:
                qq.append(cnt)
print(max(qq))

