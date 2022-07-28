from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

ocean = []

for i in range(N):
    ocean.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x,visited):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    while q:
        ty,tx = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx]:
                    if ocean[ny][nx] > 0:
                        q.append((ny,nx))
                        visited[ny][nx] = True
                    else:
                        if ocean[ty][tx] > 0:
                            ocean[ty][tx] -= 1

time = 0
                       
while True:
    visited = [[False for _ in range(M)]for __ in range(N)]

    team = 0

    for y in range(N):
        for x in range(M):
            if ocean[y][x] > 0 and not visited[y][x]:
                bfs(y,x,visited)
                team += 1

    if team > 1:
        print(time)
        break

    if team == 0:
        print(0)
        break

    time += 1