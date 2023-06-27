
def fir(n,str):
    if n==3:
        print(str * 3)
        return str*3
    else:

        fir(n/3,fir(n/3,str))
        fir(n/3,sec(n/3,str))
        fir(n/3,fir(n/3,str))
        return str*3

def sec(n,str):
    if n==3:
        print(str + " "*int(n/3) + str)
        return str + " "*int(n/3) + str
    else:
        sec(n/3,fir(n/3, str))
        sec(n/3,sec(n/3, str))
        sec(n/3,fir(n/3, str))
        return str + " "*int(n/3) + str

def star(n):
    print(fir(n,"*"))
    star(n/3)

    return

#print(fir(3,sec(3,"*")))
# fir(9,"*")
# sec(9,"*")
# fir(9,"*")


#star(27)
#star
#f
#print
#f
#s
#f
#return 문자를 주고

# #star(3)
# fir(3,"*")
# sec(3,"*")
# fir(3,"*")
#
# #star(9)
# fir(9,fir(3,"*"))
# fir(9,sec(3,"*"))
# fir(9,fir(3,"*"))
#
# sec(3,fir(3,"*"))
# sec(3,sec(3,"*"))
# sec(3,fir(3,"*"))
#
# fir(9,fir(3,"*"))
# fir(9,sec(3,"*"))
# fir(9,fir(3,"*"))

