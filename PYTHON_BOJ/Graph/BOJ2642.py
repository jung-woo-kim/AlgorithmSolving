from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

start,end = map(int,sys.stdin.readline().rstrip().split())

m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(s):
    q = deque()
    q.append(s)
    q.append(-1)
    chon = 0
    visited = [False for _ in range(n+1)]
    visited[s] = True
    while q:
        tmp = q.popleft()

        if tmp == -1:
            if q:
                chon += 1
                q.append(-1)
            else:
                return -1
        else:
            for node in graph[tmp]:
                if node == end:
                    return chon+1

                if not visited[node]:
                    visited[node] = True
                    q.append(node)

print(BFS(start))