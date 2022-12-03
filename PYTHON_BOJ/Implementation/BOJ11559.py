import sys
from collections import deque

board = []

for i in range(12):
    board.append(list(sys.stdin.readline().rstrip()))

dx = [1,0,-1,1]
dy = [0,-1,0,0]

def down():
    for y in range(11,-1,-1):
        for x in range(6):
            if board[y][x] == ".":
                for ny in range(y,-1,-1):
                    if board[ny][x] != ".":
                        board[y][x] = board[ny][x]
                        board[ny][x] = "."
                        break

def BFS(s,sy,sx):
    q = deque()
    q.append((sy,sx))
    puyo = [(sy,sx)]
    visited[sy][sx] = True
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<12 and 0<=nx<6 and not visited[ny][nx]:
                if board[ny][nx] == s:
                    q.append((ny,nx))
                    puyo.append((ny,nx))
                    visited[ny][nx] = True
 
    return puyo

answer = 0

while True:
    visited = [[False for __ in range(6)] for _ in range(12)]
    
    check = True

    for y in range(11,-1,-1):
        for x in range(6):
            if board[y][x] != ".":
                puyo = BFS(board[y][x],y,x)
                if len(puyo) >= 4:
                    check = False
                    for py,px in puyo:
                        board[py][px] = "."
    
    
    down()

    if check:
        break
    else:
        answer += 1

print(answer)