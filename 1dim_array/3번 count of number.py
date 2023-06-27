a=[int(input()) for i in range(3)]
mul=a[0] * a[1] * a[2]
mul_list=list(str(mul))
for i in range(10):
    print(mul_list.count(str(i)))

#map 함수를 사용하면 숫자형도 리스트로 반환할 수 있다
# a = int(input())
# b = int(input())
# c = int(input())
# s = list(map(int, str(a*b*c)))
# for i in range(10):
#     print(s.count(i))