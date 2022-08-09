from collections import deque
from copy import copy, deepcopy
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

visited = [[False for _ in range(M)] for __ in range(N)]

for y in range(N):
    for x in range(M):
        if board[y][x] == "W":
            visited[y][x] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(sy,sx,v):
    q = deque()
    q.append((sy,sx))
    v[sy][sx] = True
    q.append(-1)
    dist = 0


    while q:
        temp = q.popleft()
        if temp == -1:
            if q:
                dist += 1
                q.append(-1)
            else:
                return dist
        else:
            y,x = temp
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    v[ny][nx] = True
                    q.append((ny,nx))

answer = 0

for y in range(N):
    for x in range(M):
        if board[y][x] == "L":
            v = deepcopy(visited)
            answer = max(BFS(y,x,v),answer)

print(answer)
