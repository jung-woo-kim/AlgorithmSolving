from collections import deque
import sys

M, N, H = map(int,sys.stdin.readline().rstrip().split())

box = []

for _ in range(H):
    temp = []
    for __ in range(N):
        temp.append(list(map(int,sys.stdin.readline().rstrip().split())))
    box.append(temp)

dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]
dh = [-1,1,0,0,0,0]

queue = deque()

for h in range(H):
    for y in range(N):
        for x in range(M):
            if box[h][y][x] == 1:
                queue.append((h,y,x))

def bfs():
    global queue

    while queue:
        h,y,x = queue.popleft()
        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
                if box[nh][ny][nx] == 0:
                    box[nh][ny][nx] = box[h][y][x] + 1
                    queue.append((nh,ny,nx))

bfs()

answer = 0

for h in range(H):
    for y in range(N):
        for x in range(M):
            if box[h][y][x] == 0:
                print(-1)
                exit()
            else:
                answer = max(answer,box[h][y][x])

print(answer-1)
    

 