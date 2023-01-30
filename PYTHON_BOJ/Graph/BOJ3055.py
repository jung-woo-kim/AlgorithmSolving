import sys
from collections import deque

R, C = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

visited = [[False for _ in range(C)] for __ in range(R)]
water = deque()
biber = deque()
dc = [1,0,-1,0]
dr = [0,1,0,-1]

for r in range(R):
    for c in range(C):
        if board[r][c] == "D":
            d_r = r
            d_c = c
        if board[r][c] == "*":
            visited[r][c] = True
            water.append((r,c))
        if board[r][c] == "S":
            visited[r][c] = True
            biber.append((r,c))
        if board[r][c] == "X":
            visited[r][c] = True

def bfs_water():
    for _ in range(len(water)):
        r,c = water.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < R and 0<= nc < C and not visited[nr][nc]:
                if board[nr][nc] == ".":
                    visited[nr][nc] = True
                    water.append((nr,nc))
                    board[nr][nc] = "*"
time = 0
def bfs_biber():
    global time
    while biber:
        time += 1
        bfs_water()
        for _ in range(len(biber)):
            r,c = biber.popleft()
            if board[r][c] == "D":
                return True
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<= nr < R and 0<= nc < C and not visited[nr][nc]:
                    biber.append((nr,nc))
                    visited[nr][nc] = True
    
    return False

if bfs_biber():
    print(time-1)
else:
    print("KAKTUS")