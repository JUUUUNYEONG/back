a,b,c=map(int,input().split())
if c - b > 0:
    k = int(a/(c-b)) + 1
    print(k)
else:
    print(-1)