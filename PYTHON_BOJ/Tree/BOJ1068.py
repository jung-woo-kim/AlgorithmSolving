from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

temp = list(map(int,sys.stdin.readline().rstrip().split()))

## 삭제될 노드
remove = int(sys.stdin.readline().rstrip())

##그래프
graph = [[] for i in range(N)]

##BFS탐색을 위한 배열
visited = [False for _ in range(N)]

parent_node = 0

##그래프 생성 및 edge 연결
for i in range(N):
    if temp[i] != -1:
        graph[i].append(temp[i])
        graph[temp[i]].append(i)
    else:
        ##부모노드부터 탐색을 시작해야하므로 부모노드의 번호 저장
        parent_node = i

print(graph)

answer = 0

##BFS
def bfs(p):
    global answer
    q = deque()
    q.append(p)
    visited[p] = True

    while len(q) != 0:
        now = q.popleft()
        ##그래프에 연결 되어있는 곳들을 바로 탐색
        for link in graph[now]:
            ##연결 되어있는 곳이 삭제된 노드가 아니고, 이미 방문된 노드라면?
            if link != remove and not visited[link]:
                q.append(link)
                visited[link] = True
             
            if link == remove:
                ##연결되어있는 곳이 삭제된 노드인데, 지금 노드의 edge가 2개이고, 부모노드가 아니라면
                if len(graph[now]) == 2 and now != parent_node:
                    answer+=1
                ##연결되어있는 곳이 삭제된 노드인데, 지금 노드의 edge가 한개이고, 이것이 부모노드라면
                if len(graph[now]) == 1 and now == parent_node:
                    answer+=1
        ##연결된 노드가 하나이고, 부모노드가 아니라면,
        if (len(graph[now]) == 1 and now != parent_node):
            answer += 1

##부모노드를 삭제하지 않았다면,
if remove != parent_node:
    bfs(parent_node)



print(answer)
