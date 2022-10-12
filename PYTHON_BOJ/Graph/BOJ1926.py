from collections import deque
import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

drawing = []

for _ in range(n):
    drawing.append(list(map(int,sys.stdin.readline().rstrip().split())))

visited = [[False for _ in range(m)] for __ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(sy,sx):
    q = deque()
    q.append((sy,sx))
    size = 1
    visited[sy][sx] = True

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and drawing[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny,nx))
                size+=1
    return size

answer = []

for y in range(n):
    for x in range(m):
        if drawing[y][x] == 1 and not visited[y][x]:
            answer.append(BFS(y,x)) 

print(len(answer))
if len(answer) == 0:
    print(0)
else:
    print(max(answer))