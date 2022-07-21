from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for i in range(N)]

temp = []

for _ in range(M):
    A, B = map(int,sys.stdin.readline().rstrip().split())
    temp.append((A,B))
    temp.append((B,A))

temp = list(set(temp))

for A,B in temp:    
    graph[A-1].append(B-1)

def bfs(n):
    queue = deque()
    queue.append(n)
    queue.append(-1)
    check = 1 # 현재 몇번째 탐색이다.
    answer = 0
    visited = [False for _ in range(N)]
    visited[n] = True
    while queue:
        node = queue.popleft()

        if node == -1:
            if queue:
                check += 1
                queue.append(-1)
            else:
                break
        else:
            for g in graph[node]:
                if not visited[g]:
                    visited[g] = True
                    queue.append(g)
                    answer+=check
    
    return answer

m = 1e9

a = -1

for i in range(N):
    temp = bfs(i)
    if m > temp:
        m = temp
        a = i+1  
        

print(a)