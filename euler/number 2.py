# 피보나치 수열에서 4백만 이하 and 짝수인 항의 합
def Fi(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return Fi(n-2)+Fi(n-1)
total=0
for i in range(1,33):
    if Fi(i)%2==0 and Fi(i) <=4000000:
        total+=Fi(i)
print(total)
