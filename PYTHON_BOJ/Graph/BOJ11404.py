import sys


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

INF = sys.maxsize

graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a-1][b-1] = min(c,graph[a-1][b-1])

for i in range(N): #거치는 점
    for j in range(N): #시작점
        for k in range(N): # 끝점
            graph[j][k] = min(graph[j][k],graph[j][i] + graph[i][k])

for i in range(N): 
    answer = ""
    for j in range(N):
        if graph[i][j]< sys.maxsize:
            answer += str(graph[i][j])+" "
        else:
            answer += "0 "
    print(answer)