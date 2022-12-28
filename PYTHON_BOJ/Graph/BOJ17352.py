import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(N-2):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)

group_1 = []
group_2 = []
visited = [False for _ in range(N+1)]

def BFS(s,group):
    q = deque()
    q.append(s)
    visited[s] = True
    group.append(s)
    while q:
        now = q.popleft()

        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                group.append(next)
    return group
BFS(1,group_1)

for s in range(1,N+1):
    if not visited[s]:
        BFS(s,group_2)
        break

print(str(group_1[0]) + " " + str(group_2[0]))