m=int(input())
n=int(input())

table=[True] * (n+1)
result = []

for i in range(2,n+1):
    if table[i]:
        if m <= i:
            result.append(i)
        for j in range(i*2,n+1,i):
            table[j]=False
sum_rt = sum(table)

if sum_rt:
    print(sum(result))
    print(result[0])
else:
    print(-1)

#길을 물건을 가지러 갈때 어떤 물건을 집어야 하는지
#숙지하고 가면 출발지로 돌아올 필요가 없다
#출발지로 돌아오는 행위를 최대한 줄이자!