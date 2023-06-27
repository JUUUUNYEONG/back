import sys
N=int(sys.stdin.readline())
lst=sys.stdin.readline().split()
sett=sorted(set(lst),key=int,reverse=False)
dic=dict()
for idx,value in enumerate(sett):
    dic[value]=idx
for i in lst:
    print(dic[i],end=" ")

