from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(N):
    board.append(list(map(int,list(sys.stdin.readline().rstrip()))))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(sy,sx):
    q = deque()
    q.append((sy,sx))
    visited[sy][sx] = True
    move = 1
    li = []
    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M  and 0 <= ny < N:
                if not visited[ny][nx]:
                    if board[ny][nx]==0:
                        move+=1
                        visited[ny][nx] = True
                        q.append((ny,nx))
                    if board[ny][nx]!=0:
                        li.append((ny,nx))
    return move,set(li)

visited = [[False for _ in range(M)]for _ in range(N)]

for y in range(N):
    for x in range(M):
        if board[y][x] == 0 and not visited[y][x]:
            move,li = BFS(y,x)
            for ny,nx in li:
                board[ny][nx] += move
   
for y in range(N):
    temp = ""
    for x in range(M):
        temp += str(board[y][x])
    print(temp)
