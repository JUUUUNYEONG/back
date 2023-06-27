#대칭수 만들기 이거는 ㄷㄷ
a=789456
l1=[]
for i in range(100,1000):
    for j in range(100,1000):
        if len("{0}".format(i*j))==4:
            if "{0}".format(i*j)[0]=="{0}".format(i*j)[3] and "{0}".format(i*j)[1]=="{0}".format(i*j)[2]:
                l1.append(i*j)
        elif len("{0}".format(i*j))==5:
            if "{0}".format(i * j)[0] == "{0}".format(i * j)[4] and "{0}".format(i * j)[1] == "{0}".format(i * j)[3]:
                l1.append(i*j)
        elif len("{0}".format(i*j))==6:
            if "{0}".format(i*j)[0]=="{0}".format(i*j)[5] and "{0}".format(i*j)[1]=="{0}".format(i*j)[4] and "{0}".format(i*j)[2] == "{0}".format(i*j)[3]:
                l1.append(i*j)


print((l1))