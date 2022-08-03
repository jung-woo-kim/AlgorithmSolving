from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = []

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def BFS():
    q = deque()
    q.append((0,0))
    visited = [[0 for _ in range(M)]for __ in range(N)]
    visited[0][0] = 1
    cheese = []
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0:
                    if board[ny][nx] == 1:
                        visited[ny][nx] += 2
                    else:
                        visited[ny][nx] += 1
                        q.append((ny,nx))
                elif visited[ny][nx] == 1:
                    pass
                elif visited[ny][nx] == 2:
                    #두번째 접촉
                    cheese.append((ny,nx))
    return cheese

answer = 0

while True:
    answer += 1
    cheese = BFS()
    for y,x in cheese:
        board[y][x] = 0
    if len(cheese) == 0:
        print(answer-1)
        exit()
