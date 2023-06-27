#문자열을 저장하는 용도로 만들어줍니다.
def star(n):
    first(n)
    second(n)
    first(n)

def first(n):
    if n==3:
        print("***")
        return "***"
    else:
        print(first(n/3))
        print(second(n/3))
        print(first(n/3))
        return first(n/3)*3

def second(n):
    if n==3:
        print("* *")
        return "* *"
    else:
        print(first(n/3) + " "*3 + first(n/3))
        print(second(n/3) + " "*3 + second(n/3))
        print(first(n/3) + " " *3 + first(n/3))
        return second(n/3) + " "*int(n/3) + second(n/3)
star(3)
#star(3)
#f(3)
#star(1)
#s(3)
#star(1)
#f(3)
#star(1)

#star(9)
#f(9)
#star(3)
#f(3)
#star(1)
#s(3)
#star(1)
#f(3)
#star(1)