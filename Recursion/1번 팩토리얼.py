def func_fac(N):
    if not N: return 1
    else: return N * func_fac(N-1)
print(func_fac(int(input())))