a=list(input().lower())

cnt_l=[]
for i in set(a):
    m = a.count(i)
    cnt_l += [m]
    if max(cnt_l) <= m:
        value = i
k = cnt_l.count(max(cnt_l))

if k == 1:
    print(value.upper())
else:
    print("?")

# cnt_l=[]
# for i in set(a):
#     cnt_l.append(a.count(i))
#     if max(cnt_l) <= a.count(i):
#         value = i
# k = cnt_l.count(max(cnt_l))
#
# if k == 1:
#     print(value.upper())
# else:
#     print("?")
