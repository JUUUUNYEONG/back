b=0
def func_chat(N):
    global b
    if N==0:
        a='_'*4*b
        print(a+'"재귀함수가 뭔가요?"\n'+a+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        return N - func_chat(N-1)
    elif N<0:
        if b<0:
            return 0
        a='_'*4*b
        print(a+'라고 답변하였지.')
        b-=1
        return N - func_chat(N-1)
    else:
        a='_'*4*b
        print(a+'"재귀함수가 뭔가요?"\n'+
              a+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'+
              a+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'+
              a+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        b+=1
        return N - func_chat(N-1)
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
func_chat(int(input()))
