import sys
N=int(sys.stdin.readline())
lst=[int(sys.stdin.readline()) for i in range(N)]
output_range=[0] * N
sol_idx=sorted(list(set(lst)))
sol_cnt=[]

for i in sol_idx:
    sol_cnt.append(lst.count(i))
for i in range(len(sol_cnt)-1):
    sol_cnt[i+1]=sol_cnt[i]+sol_cnt[i+1]
for i in range(len(lst)):
    k=lst.pop()
    indx=sol_idx.index(k)
    output_range[sol_cnt[indx]-1]=k
    sol_cnt[indx]=sol_cnt[indx]-1
for i in output_range:
    print(i)