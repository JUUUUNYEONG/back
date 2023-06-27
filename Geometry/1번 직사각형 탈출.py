import sys
x,y,w,h=map(int,sys.stdin.readline().rstrip().split())
print(min(h-y,y,w-x,x))