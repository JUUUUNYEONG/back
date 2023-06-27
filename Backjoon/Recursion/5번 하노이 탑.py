def hanoi(n,_from=1,_to=3):
    if not n:
        return
    else:
        k=[1,2,3]
        k.remove(_from)
        k.remove(_to)
        hanoi(n-1,_from,k[0])
        print(_from,_to)
        hanoi(n-1,k[0],_to)

def func_cnt(n):
    if n==1:
        return 1
    else:
        return func_cnt(n-1)*2 + 1
N=int(input())
print(func_cnt(N))
hanoi(N)
