import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 1e9

visited = [False for _ in range(N)]

def dfs(start,depth,cost):
    global answer

    if depth == N:
        answer = min(answer,cost)
    
    for node in range(N):
        if not visited[node]:
            visited[node] = True
            dfs(node,depth+1,cost+graph[start][node])
            visited[node] = False

visited[K] = True

dfs(K,1,0)
print(answer)