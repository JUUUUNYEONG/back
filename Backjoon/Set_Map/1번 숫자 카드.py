import sys
N1=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().rstrip().split()))
st={x for x in lst}
N2=int(sys.stdin.readline())
lst2=list(map(int,sys.stdin.readline().rstrip().split()))
for i in lst2:
    print(int(i in st),end=" ")