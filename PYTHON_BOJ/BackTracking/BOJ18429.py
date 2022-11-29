import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

weight = 500

kit = list(map(int,sys.stdin.readline().rstrip().split()))

visited = [False for i in range(N)]
answer = 0
def DFS(depth,weight):
    global answer
    if depth == N-1:
        answer += 1

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            weight -= K
            weight += kit[i]
            if weight >= 500:
                DFS(depth+1,weight)
            weight += K
            weight -= kit[i]
            visited[i] = False
DFS(0,500)
print(answer)