import sys
N=int(sys.stdin.readline())
def check(x,l):
    st="".join(x*2)
    lt=l*2
    idx=0
    if "4242" in st:
        idx = st.find("24")
        w = int(lt[st.find("1")]) * int(lt[st.find("3")]) - int(lt[idx])*int(lt[idx+1])
    elif "2323" in st:
        idx = st.find("32")
        w = int(lt[st.find("1")]) * int(lt[st.find("4")]) - int(lt[idx])*int(lt[idx+1])
    elif "3131" in st:
        idx = st.find("13")
        w = int(lt[st.find("2")]) * int(lt[st.find("4")]) - int(lt[idx])*int(lt[idx+1])
    elif "1414" in st:
        idx = st.find("41")
        w = int(lt[st.find("2")]) * int(lt[st.find("3")]) - int(lt[idx])*int(lt[idx+1])
    return w

direction=[]
length=[]
for i in range(6):
    d,l=sys.stdin.readline().rstrip().split()
    direction.append(d)
    length.append(l)

print(N*check(direction,length))

#4 2 3 1
#4 2 3 1 3 1
#위로 4 아래로 3 오른쪽 1 왼쪽 2
#4 2 4 2 3 1 [4 2반복] 4 2 ㄴ모양 5가 반환되면 길이 값은 5,0을 반환해야한다
#2 3 2 3 1 4 [2 3반복] 2 3 _ㅣ 모양
#2 3 1 3 1 4 [3 1반복] 3 1 ㄱ 모양
#2 3 1 4 1 4 [1 4반복] 1 4 ㅣ- 모양