def check_string(string,start_str):
    List=[0 for i in range(len(string))]
    if start_str:
        for i in range(len(string)):
            if i%2==0 and string[i]=="B":
                List[i]=1
            elif i%2==1 and string[i]=="W":
                List[i]=1
    else:
        for i in range(len(string)):
            if i % 2 == 0 and string[i] == "W":
                List[i] = 1
            elif i % 2 == 1 and string[i] == "B":
                List[i] = 1
    return List

k=list(map(int,input().split()))
chk=0
LB=[]
LW=[]
LR=[]
for i in range(k[0]):
    string=input()
    LB.append(check_string(string,chk%2))
    LW.append(check_string(string,(chk+1)%2))
    chk+=1
for j in range(k[1]-7):
    cnt=0
    for i in range(k[0]-7):
        result=0
        for l in range(i,i+8):
            result += sum(LB[l][j:j+8])
        LR.append(result)
        cnt+=1
for j in range(k[1]-7):
    cnt=0
    for i in range(k[0]-7):
        result=0
        for l in range(i,i+8):
            result += sum(LW[l][j:j+8])
        LR.append(result)
        cnt+=1
print(min(LR))