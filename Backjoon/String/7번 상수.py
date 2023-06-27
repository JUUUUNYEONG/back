a,b=input().split()
a=a[::-1]
b=b[::-1]
print(max(int(a),int(b)))

#동적으로 if문 사용하는 법
#print(int(a)) if int(a) > int(b) else print(int(b))