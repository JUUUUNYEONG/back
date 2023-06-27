a=int(input())
i=1
while True:
    subs = (i * (i + 1)) / 2
    i += 1
    if a <= subs:
        break
dif = subs - a
if i%2 == 1:
    print("{0}/{1}".format(int(i - 1 - dif), int(dif + 1)))
else:
    print("{0}/{1}".format(int(dif+1),int(i-1-dif)))