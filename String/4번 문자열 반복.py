a=int(input())
for i in range(a):
    b=input().split()
    b_l=list(map(lambda x: x * int(b[0]), b[1]))
    print("".join(b_l))

#수정 후 입력받는 변수를 2개로 늘렸다.
# for i in range(a):
#     R,S=input().split()
#     b_l=list(map(lambda x: x * int(R), S))
#     print("".join(b_l))
