H,M=map(int,input().split())
T=int(input())
D=M+T
if D>=60:
    H+=D//60
    D%=60
    if H>23:
        H-=24
print(H,D)