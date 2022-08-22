from collections import deque
import sys

N, M, K = map(int,sys.stdin.readline().rstrip().split())

board = [sys.stdin.readline().rstrip() for _ in range(N)]

visited = [[[False for _ in range(K+1)]for __ in range(M)]for ___ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

#0이면 낮 1이면 밤
def BFS():
    q = deque()
    q.append((0,0,K,1))
    visited[0][0][K] = True
    day = 1
    while q:
        night = False if day > 0 else True

        for _ in range(len(q)):
            y,x,wall,dist = q.popleft()
            if y == N-1 and x == M-1:
                return dist


            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<M and 0<=ny<N:
                    if board[ny][nx] == '0' and not visited[ny][nx][wall]:
                        q.append((ny,nx,wall,dist+1))
                        visited[ny][nx][wall] = True
                    elif board[ny][nx] == '1' and wall > 0 and not visited[ny][nx][wall-1]:
                        if not night:
                            q.append((ny,nx,wall-1,dist+1))
                            visited[ny][nx][wall-1] = True
                        else:
                            q.append((y,x,wall,dist+1))
        day = day + 1 if day > 0 else day - 1
        day *= -1
        
    return -1

print(BFS())