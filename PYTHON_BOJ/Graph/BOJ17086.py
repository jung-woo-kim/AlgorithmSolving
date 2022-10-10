from collections import deque
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def BFS(sy,sx):
    q = deque()
    q.append((sy,sx,0))
    visited = [[False for _ in range(M)] for __ in range(N)]
    visited[sy][sx] = True

    while q:
        y,x,now = q.popleft()

        if board[y][x] == 1:
            return now

        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<N and 0<=nx<M:
                visited[ny][nx] = True
                q.append((ny,nx,now+1))

answer = 0

for y in range(N):
    for x in range(M):
        answer = max(answer,BFS(y,x))

print(answer)