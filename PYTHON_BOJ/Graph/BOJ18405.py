import sys
from collections import deque


N,K = map(int,sys.stdin.readline().rstrip().split())
dx = [1,0,-1,0]
dy = [0,-1,0,1]

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

S,X,Y = map(int,sys.stdin.readline().rstrip().split())

q = deque()

def BFS():
    time = 0
    while q and time < S:
        time += 1
        for _ in range(len(q)):
            now,y,x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
                    board[ny][nx] = now
                    q.append((now,ny,nx))

for y in range(N):
    for x in range(N):
        if board[y][x] != 0:
            q.append((board[y][x],y,x))
q = sorted(q)
q = deque(q)
BFS()

print(board[X-1][Y-1])
