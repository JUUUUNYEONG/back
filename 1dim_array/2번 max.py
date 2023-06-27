mylist=[]
for i in range(9):
    a=int(input())
    mylist.append(a)
print("%s\n%s"%(max(mylist),mylist.index(max(mylist))+1))

# lst = [int(input()) for i in range(9)]
# print(max(lst))
# print(lst.index(max(lst))+1)