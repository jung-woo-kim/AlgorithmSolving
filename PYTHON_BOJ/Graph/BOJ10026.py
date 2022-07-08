from collections import deque
import sys

N = int(sys.stdin.readline())

painting = [sys.stdin.readline().rstrip() for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs_1(y,x):
    queue = deque()
    queue.append((y,x))
    paint = painting[y][x]
    while queue:
        ty,tx = queue.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N and not visited[ny][nx]:
                    # print("x : "+str(nx) + " y :" + str(ny))
                    # print(painting[ny][nx])
                    # print(paint)
                if painting[ny][nx] == paint:
                    visited[ny][nx] = True
                    queue.append((ny,nx))
 
answer_1 = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            visited[y][x] = True          
            bfs_1(y,x)
            answer_1+=1

visited = [[False for _ in range(N)] for _ in range(N)]
answer_2 = 0

def bfs_2(y,x):
    queue = deque()
    queue.append((y,x))
    paint = painting[y][x]
    if paint == 'R' or paint == 'G':
        paint = 1
    else:
        paint = 0
    while queue:
        ty,tx = queue.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N and not visited[ny][nx]:
                    # print("x : "+str(nx) + " y :" + str(ny))
                    # print(painting[ny][nx])
                    # print(paint)
                temp = -1
                if painting[ny][nx] == 'R' or painting[ny][nx] == 'G':
                    temp = 1
                else:
                    temp = 0
                if temp == paint:
                    visited[ny][nx] = True
                    queue.append((ny,nx))

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            visited[y][x] = True          
            bfs_2(y,x)
            answer_2+=1

print(str(answer_1)+" "+str(answer_2))
