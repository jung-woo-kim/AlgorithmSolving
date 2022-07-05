import sys


N = int(sys.stdin.readline())

visited = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

cnt = 0

##pipe가 0이면 가로 1면 대각선 2이면 세로
def dfs(x,y,pipe):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return
    
    if pipe == 0:
        ##가로면 대각선이랑 가로만 됨

        if x+1 < N and visited[y][x+1] == 0:
            dfs(x+1,y,0)

        if x+1 < N and y+1 <N and visited[y+1][x+1] == 0 and visited[y+1][x] == 0 and visited[y][x+1] == 0:
            dfs(x+1,y+1,1)
                    
    elif pipe == 1:
        if x+1 < N and visited[y][x+1] == 0:
            dfs(x+1,y,0)
        if x+1 < N and y+1 <N and visited[y+1][x+1] == 0 and visited[y+1][x] == 0 and visited[y][x+1] == 0:
            dfs(x+1,y+1,1)
        if y+1 <N and visited[y+1][x] == 0:
            dfs(x,y+1,2)
                       
    
    elif pipe == 2:
        if x+1 < N and y+1 <N and visited[y+1][x+1] == 0 and visited[y+1][x] == 0 and visited[y][x+1] == 0:
            dfs(x+1,y+1,1)

        if y+1 <N and visited[y+1][x] == 0:
            dfs(x,y+1,2)
                     


dfs(1,0,0)
print(cnt)