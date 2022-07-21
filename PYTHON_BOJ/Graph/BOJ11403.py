from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N)]

for i in range(N):
    node = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if node[j] == 1:
            graph[i].append(int(j))

def bfs(node):
    queue = deque()
    queue.append(node)
    visited = [False for _ in range(N)]
    #visited[node] = True -> 순환 시 다시 나한테도 와야함
    answer = []
    while queue:
        n = queue.popleft()

        for nod in graph[n]:
            if not visited[nod]:
                queue.append(nod) 
                answer.append(nod)
                visited[nod] = True

    return answer


for i in range(N):
    node = bfs(i)
    answer = ['0' for _ in range(N)]
    for n in node:
        answer[n] = '1'
    print(" ".join(answer))