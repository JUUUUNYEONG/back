import sys
N=int(sys.stdin.readline())
lst=[int(sys.stdin.readline()) for _ in range(N)]
cnt=[1]
for i in sorted(list(set(lst))):
    if cnt[0] < lst.count(i):
        cnt=[1]
        cnt[0]=lst.count(i)
        cnt.append(i)
    elif cnt[0] == lst.count(i):
        cnt.append(i)

print(round(sum(lst)/N))
print(sorted(lst)[N//2])
if len(cnt)==2:
    print(cnt[1])
else:
    print(cnt[2])
print(max(lst)-min(lst))