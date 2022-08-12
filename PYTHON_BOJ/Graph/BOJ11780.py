import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

INF = sys.maxsize

graph = [[[INF,str(i+1)] for i in range(n)] for _ in range(n)]

for i in range(n):
    graph[i][i][0] = 0

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    if graph[a-1][b-1][0] > c:
        graph[a-1][b-1][0] = c
        graph[a-1][b-1][1] = str(a) +" "+str(b)
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k][0] > graph[j][i][0] + graph[i][k][0]:
                graph[j][k][0] = graph[j][i][0] + graph[i][k][0]
                
                graph[j][k][1] = graph[j][i][1] +" "+" ".join(graph[i][k][1].split()[1:]) 


for i in range(n):
    temp = ""
    for j in range(n):
        if graph[i][j][0] == INF:
            temp += "0 "
        else:
            temp += str(graph[i][j][0]) + " "
    print(temp) 

for i in range(n):
    for j in range(n):
        temp = ""
        if i == j:
            print(0)
        elif len(graph[i][j][1].split()) < 2:
            print(0)
        else:
            temp += str(len(graph[i][j][1].split())) + " "
            temp += graph[i][j][1]
            print(temp)