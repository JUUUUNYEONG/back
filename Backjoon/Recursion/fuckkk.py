def starr(n):
    if n==1:
        return
    else:
        starr(n/3)
        print("*")
        starr(n/3)
def start_line(n,str):
    if n==1:
        return str
    else:
        return start_line(n/3,str) * 3
def middle_line(n,str):
    if n==1:
        return str
    else:
        return middle_line(n/3,str) + " "*int(n/3) + middle_line(n/3,str)
print(start_line(9,"*"))
print(middle_line(9,"***"))


def star(n):
    if n==1:
        return
    else:
        start_line(n)
        middle_line(n)
        start_line(n)