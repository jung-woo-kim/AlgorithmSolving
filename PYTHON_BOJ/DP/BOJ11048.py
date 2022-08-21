from collections import deque
import sys

N,M =map(int,sys.stdin.readline().rstrip().split())

maze = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[-1 for _ in range(M)] for __ in range(N)]
dp[0][0] = maze[0][0]

dx = [0,1,1]
dy = [1,0,1]

def BFS():

    q = deque()
    q.append((0,0))

    while q:
        y,x = q.popleft()

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N:
                if dp[y][x] + maze[ny][nx] > dp[ny][nx]:
                    dp[ny][nx] = dp[y][x] + maze[ny][nx]
                    q.append((ny,nx))
              

BFS()


print(dp[-1][-1])
    
