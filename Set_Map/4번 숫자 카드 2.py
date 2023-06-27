import sys
N=sys.stdin.readline()
A=sys.stdin.readline().rstrip()
M=sys.stdin.readline()
B=sys.stdin.readline().rstrip()
dic={}
for i in list(A.split()):
    if i in dic:
        dic[i]=dic[i]+1
        continue
    dic[i]=1
print(" ".join(map(lambda x: str(dic[x]) if x in dic else '0',list(B.split()))))