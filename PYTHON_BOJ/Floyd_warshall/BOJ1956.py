import sys

V,E = map(int,sys.stdin.readline().rstrip().split())

graph = [[1e9 for _ in range(V+1)] for _ in range(V+1)]

answer = 1e9

for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a][b] = min(graph[a][b],c)

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
for i in range(1,V+1):
    answer = min(graph[i][i],answer)

if answer == 1e9:
    print(-1)
else:
    print(answer)