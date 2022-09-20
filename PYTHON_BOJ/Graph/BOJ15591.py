from collections import deque
import sys

N,Q = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,sys.stdin.readline().rstrip().split())
    graph[p].append((q,r))
    graph[q].append((p,r))

def BFS(n,K):
    q = deque()
    q.append((n,1e9))
    visited = [False for _ in range(N+1)]
    visited[n] = True
    answer = []

    while q:
        node,weight = q.popleft()
        if weight >= K:
            answer.append(node)
        for i,w in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i,min(weight,w)))
    
    return len(answer)

for _ in range(Q):
    k,v = map(int,sys.stdin.readline().rstrip().split())
    print(BFS(v,k)-1)
