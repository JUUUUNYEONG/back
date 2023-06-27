import sys
while True:
    x=sorted(list(map(int,sys.stdin.readline().rstrip().split())))
    if x[0]==0:
        break
    if x[0]**2+x[1]**2==x[2]**2:
        print("right")
    else:
        print("wrong")