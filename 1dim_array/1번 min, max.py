a=int(input())
b=input()
maxlist=b.split(" ")
mylist=[]
for i in maxlist:
    mylist.append(int(i))
print(min(mylist),max(mylist))

#b=map(int,input().split())
#print(max(list(b)))