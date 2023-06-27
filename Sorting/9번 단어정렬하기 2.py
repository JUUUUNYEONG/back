import sys
N=int(sys.stdin.readline())
my_set=set()
for _ in range(N):
    x=sys.stdin.readline().rstrip()
    my_set.add(x)
lst=sorted(list(my_set))
for i in sorted(lst,key=len):
    print(i)