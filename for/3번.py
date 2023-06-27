import sys
input=sys.stdin.readline()
n=int(input)
s=0
for i in range(n+1):
    s+=i
print(s)