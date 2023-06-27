import sys; input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))
N,M,V = map(int, input().split())
#visit = [[False for j in range(N+1)] for i in range(N+1)] #양방향인 경우
visit1 = [False for j in range(N+1)]
visit2 = [False for k in range(N+1)]
graph = [[] for i in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

class Graph:
    def __init__(self,graph,start,visit1,visit2):
        self.stack =[]
        self.queue = []
        self.graph = graph
        self.start = start
        self.visit1 = visit1
        self.visit2 = visit2

    def dfs(self):
        current= self.start #처음 출발 정점을 잡는다!
        self.stack.append(current) #처음 출발 정점을 stack 구조에 삽입한다.
        while len(self.stack) > 0: #stack이 빌때까지 돌린다. // 1에 인접한 애들을 전부 다 stack에 넣고 왔다. 순서는 맞다고 가정!
            curNode = self.stack.pop() #stack에 있는 정점을 꺼내온다. // 1에 인접한 친구 중에서 가장 우선순위가 높은 애를 curNode로!
            if self.visit1[curNode] == False:#stack에서 방문한 정점 출력, 1 출력 됨. / #방문한 정점 출력
                print(curNode, end=" ")
            self.visit1[curNode] = True #꺼낸 정점을 visit 배열에 넣는다. visit[1] = True  // curNode의 방문 기록을 남긴다!
            for v in sorted(graph[curNode],reverse=True): #1과 연결된 정점을 확인 해야한다. graph[1] -> [2,3,4]가 있다.
                if not visit1[v]: #visit[2] =False->방문한적이 없다! 그럼 그 정점을 stack에 대입한다! // [3,4]가 되는데 이때 다시 저장한다. 1은 있으니까 제외
                    self.stack.append(v) #방문한적도 없고 연결된 정점을 모두 stack에 대입했다. // 2번째에서도 다시 대입

    def bfs(self):
        print(self.start, end=" ")
        queue = self.queue #스택 구조 생성
        for item in sorted(self.graph[self.start]): #처음 시작 정점에 있는 애들을 큐에 삽입
            queue.append(item) #모두 삽입
        self.visit2[self.start] = True
        while len(queue) > 0: #큐 자료 구조가 빌때까지
            item = queue.pop(0) #선입 선출, 맨 앞에 있는 아이템 추출
            if not self.visit2[item]: #맨 앞에 있는 아이템이 방문 한적이 없는 애라면.//
                for _item in sorted(self.graph[item]): #맨 앞에 있는 아이템이 가지고 있는 인접 노드를
                    queue.append(_item) #전부 큐에 넣는다.
                self.visit2[item] = True #그리고 방문 기록을 남긴다.
                print(item, end=" ") #방문했으니까 print

g = Graph(graph,V,visit1,visit2)
g.dfs()
print("")
g.bfs()
