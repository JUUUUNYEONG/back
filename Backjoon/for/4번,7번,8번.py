import sys
T=int(sys.stdin.readline())
for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #{0}: {2} + {3} = {1}".format(i+1,a+b,a,b))


