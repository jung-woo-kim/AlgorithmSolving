from collections import deque
from copy import deepcopy
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = []

for i in range(N):
    board.append(list(map(int,list(sys.stdin.readline().rstrip()))))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[False for _ in range(M)] for __ in range(N)]

answer = 1e9

def bfs_before():
    global answer
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    queue.append(-1)
    time = 1
    while queue:
        temp = queue.popleft()

        if temp == -1:
            if queue:
                time += 1
                queue.append(-1)
            else:
                return
        else:
            y,x = temp
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        if ny == N-1 and nx == M-1:
                            answer = min(answer,time+1)
                        if board[ny][nx] == 1:
                            bfs_after(ny,nx,visited,time+1)
                        else:
                            queue.append((ny,nx))

def bfs_after(by,bx,visited_after,time):
    global answer
    queue = deque()
    queue.append((by,bx))
    queue.append(-1)
    time_after = time
    new_visited = deepcopy(visited_after)

    while queue:
        temp = queue.popleft()

        if temp == -1:
            if queue:
                time_after += 1
                queue.append(-1)
            else:
                return
        else:
            y,x = temp
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if not new_visited[ny][nx] and board[ny][nx] != 1:
                        new_visited[ny][nx] = True
                        if ny == N-1 and nx == M-1:
                            answer = min(answer,time_after+1)
                        queue.append((ny,nx))

bfs_before()
if N == 1 and M == 1:
    print(1)
    exit()
if answer == 1e9:
    print(-1)
else:
    print(answer)