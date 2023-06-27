#어떤 수의 소수를 구하는 방법
def fac(x):
    d=2
    while d<= x:
        if x%d==0:
            print(d)
            x=x/d
        else:
            d=d+1

fac(600851475143)
#다른 사람이 풀어줌

