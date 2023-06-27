#print("**",end="")
#print("**")
#f(N) f(N/3) f(N/3/3)
f1="*"

def f(n):
    a=0
    if n==1:
        return "*"
    if n==3:
        f(3) = "f(1)*3 \n ((f(1)+" "*1)+f(1)) \n f(1)*3"
        return pass
    if n==9:
        f(3)*3 + ((f(3)+" "*3)+f(3)) + f(3)*3
    else:
        f(n/3)

print(f(1))