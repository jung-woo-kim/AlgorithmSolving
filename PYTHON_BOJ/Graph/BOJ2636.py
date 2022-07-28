from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = []

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[False for _ in range(M)]for __ in range(N)]
    cheese = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if board[ny][nx] == 1:
                        board[ny][nx] = 0
                        cheese += 1
                    else:
                        q.append((ny,nx))
    return cheese

time = 0
temp = 0
while True:
    c = bfs()
    time += 1
    
    if c == 0:
        print(time-1)
        print(temp)
        break

    temp = c
