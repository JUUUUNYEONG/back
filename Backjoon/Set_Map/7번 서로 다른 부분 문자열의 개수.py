import sys
string=sys.stdin.readline().rstrip()
st=set()
for i in range(len(string)):
    for j in range(0,len(string)-i):
        st.add(string[j:j+i+1])
print(len(st))
