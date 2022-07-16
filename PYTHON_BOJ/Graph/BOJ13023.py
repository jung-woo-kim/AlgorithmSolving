import sys

N,M =  map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


answer = 0

def dfs(depth,n):
    global answer
    print(n)
 
    if depth == 5:
        print("ck")
        print(visited)
        if not visited[n]:
            print(1)
            exit()

    for node in graph[n]:
        if not visited[node]:
            visited[node] = True
            dfs(depth+1,node)
            visited[node] = False

for node in range(N):
    visited = [False for _ in range(N)]
    visited[node] = True
    dfs(1,node)
print(0)