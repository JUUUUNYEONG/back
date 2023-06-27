def func_fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return func_fib(N-2)+func_fib(N-1)
print(func_fib(int(input())))