from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = []

for i in range(N):
    board.append(list(map(int,list(sys.stdin.readline().rstrip()))))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[[False,False] for _ in range(M)] for __ in range(N)]

answer = -1

def bfs():
    global answer
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = True
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
            y,x,n = temp
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[ny][nx][n]:
                        visited[ny][nx][n] = True
                        if ny == N-1 and nx == M-1:
                            answer = time+1
                            return

                        if board[ny][nx] == 1:
                            if n == 0:
                                queue.append((ny,nx,1))
                        else:
                            queue.append((ny,nx,n))

bfs()
print(answer)