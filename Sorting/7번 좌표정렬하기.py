import sys
N=int(sys.stdin.readline())
lst=[]
x_list=[0]*200001
cnt=0
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    x_list[x+100000]+=1
    num=str(x)+"."+str(y+100000)+"1"
    lst.append(float(num))

for i in x_list:
    if i==1:
        sol=str(sorted(lst)[cnt]).split(".")
        print(sol[0],int(sol[1])-100000)
        cnt+=1
    elif i>=2:
        y_list=[]
        for j in sorted(lst)[cnt:cnt+i]:
            y_list.append(int(str(j).split(".")[1])-100000)
        for k in sorted(y_list):
            print(str(sorted(lst)[cnt]).split(".")[0],k)
        cnt+=i