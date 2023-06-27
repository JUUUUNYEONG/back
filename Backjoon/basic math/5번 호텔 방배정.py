a=int(input())
for i in range(a):
    h,w,n=map(int,input().split())

    if n%h==0:
        xx=n//h
        yy=h
    else:
        xx=n//h+1
        yy=n%h

    if xx // 10 == 0:
        print("{0}0{1}".format(yy,xx))
    else:
        print("{0}{1}".format(yy,xx))