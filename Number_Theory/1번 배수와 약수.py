while True:
    a,b=map(int,input().split())
    if a and b:
        if b%a==0:
            print("factor")
        elif a%b==0:
            print("multiple")
        else:
            print("neither")
    else: break

while True:
    a,b=map(int, input().split())
    if not a and b: break
    if b%a==0:print("factor")
    else:print(["multiple","neither"][a%b>0]) #리스트 인덱싱으로 출력값을 뽑아냄냄