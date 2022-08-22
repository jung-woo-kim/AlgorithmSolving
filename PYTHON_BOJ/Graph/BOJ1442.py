from collections import deque
import sys

N, M, K = map(int,sys.stdin.readline().rstrip().split())

board = [sys.stdin.readline().rstrip() for i in range(N)]

visited = [[[False for _ in range(K+1)] for __ in range(M)] for ___ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS():
    q = deque()
    q.append((0,0,K,0))

    while q:
        y,x,wall,time = q.popleft()

        if y == N-1 and x == M-1:
            print(time+1)
            exit()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=ny<N and 0<=nx<M:
             
                if board[ny][nx] == "0" and not visited[ny][nx][wall]:
                    visited[ny][nx][wall] = True
                    q.append((ny,nx,wall,time+1))
                elif board[ny][nx] == "1" and wall > 0 and not visited[ny][nx][wall-1]:
                        nw = wall -1
                        visited[ny][nx][nw] = True
                        q.append((ny,nx,nw,time+1))

BFS()
print(-1)
