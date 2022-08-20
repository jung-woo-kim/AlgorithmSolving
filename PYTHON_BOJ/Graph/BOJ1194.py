from collections import deque
from copy import copy, deepcopy
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = [sys.stdin.readline().rstrip() for _ in range(N)]

for y in range(N):
    for x in range(M):
        if board[y][x] == "0":
            now_x = int(x)
            now_y = int(y)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[[0 for _ in range(64)] for _ in range(M)] for __ in range(N)]

def BFS():
    q = deque()
    q.append((now_y,now_x,0,0))
    visited[now_y][now_x][0] = 1 
    while q:
        y,x,key,now = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx][key] == 0:
                 
                    if board[ny][nx] == "." or board[ny][nx] == "0":
                        visited[ny][nx][key] = 1
                        q.append((ny,nx,key,now+1))
                    elif "a" <= board[ny][nx] <= "f":
                        st = bin(key)[2:]
                        temp = ""
                        for _ in range(6-len(st)):
                            temp += "0"
                        temp = temp + st
                        st = list(temp)
                        st[ord(board[ny][nx]) - 97] = '1'
                        k = int("".join(st),2)
                        visited[ny][nx][k] = 1
                        q.append((ny,nx,k,now+1))
                    elif "A" <= board[ny][nx] <= "F":
                        st = bin(key)[2:]
                        temp = ""
                        for _ in range(6-len(st)):
                            temp += "0"
                        temp = temp + st
                        if temp[ord(board[ny][nx]) - 65] == '1':
                            visited[ny][nx][key] = 1
                            q.append((ny,nx,key,now+1))
                    elif board[ny][nx] == "1":
                        print(now+1)
                        exit()


BFS()
print(-1)
                        

            