a=list(input().split())
while " " in a:
    a.remove(" ")
print(len(a))
#split()은 디폴트가 모든 공백을 없애주네요;;
# a=input().split()
# print(a)