import sys

M,N = map(int,sys.stdin.readline().rstrip().split())

map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer = 0

def dfs(n,x,y):

    if x == N-1 and y == M-1:
        return 1

    ##이미 방문한 길이면,
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < N and ny >= 0 and ny < M:
        
            if map[ny][nx] < n:
                print(map[ny][nx])
                dp[y][x] += dfs(int(map[ny][nx]),nx,ny)
    return dp[y][x]


print(dfs(map[0][0],0,0))
print(dp)
