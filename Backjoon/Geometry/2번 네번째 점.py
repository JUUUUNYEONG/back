import sys
lst1=[]
lst2=[]
for i in range(3):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    lst1.append(x)
    lst2.append(y)
lst1.sort()
lst2.sort()
print(lst1[0] if lst1.count(lst1[0])==1 else lst1[2],lst2[0] if lst2.count(lst2[0])==1 else lst2[2])
