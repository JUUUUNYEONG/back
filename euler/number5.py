#1~20중에서 어떤 수로도 나눌 수 있는 가장 작은 수
n=1
for i in range(2,21):
    if n%i==0:continue
    elif n*2%i==0:
        n=n*2
        continue
    elif n*3%i==0:
        n=n*3
        continue
    else:
        n=n*i
print(n)