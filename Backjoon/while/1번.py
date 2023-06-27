import sys
while True:
    a,b=map(int, sys.stdin.readline().split())
    if a!=0 or b!=0:
        print(a+b)
    else:
        break