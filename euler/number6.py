#1~100까지의 제곱의 합과 합의 제곱간의 차
A=0
B=0
for i in range(1,101):
    A=A+i**2
for i in range(1,101):
    B=B+i
print(B**2-A)