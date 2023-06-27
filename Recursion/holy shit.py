def star1(n):
    if n==1:
        return "*"
    else:
        return star1(n/3)*3
        # star2(n/3)*3
        # star1(n/3)*3

def star2(n):
    if n==1:
        return "*"
    else:
        k=" "*int(n/3)
        return k.join(star2(n/3)*2)
print(star1(9))
print(star2(9))
    #k.join(star1(n/3))
    #k.join(star2(n/3))
    #k.join(star1(n/3))


#print(star(9))
