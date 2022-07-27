from collections import deque
import sys

N, M, T = map(int,sys.stdin.readline().rstrip().split())

castle = []

for i in range(N):
    castle.append(list(map(int,sys.stdin.readline().rstrip().split())))

gram = (0,0)

for i in range(N):
    for j in range(M):
        if castle[i][j] == 2:
            gram = (i,j)

visited = [[False for _ in range(M)] for __ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

gram_time = 1e9
no_gram_time = 1e9


def bfs():
    global gram_time
    global no_gram_time
    queue = deque()
    queue.append((0,0))
    queue.append(-1)
    visited[0][0] = True
    time = 0
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
                    if not visited[ny][nx] and castle[ny][nx] != 1:
                       
                        if castle[ny][nx] == 2:
                            gram_time = time+1 + abs((M-1)-nx) + abs((N-1)-ny)
                        if ny == N-1 and nx == M-1:
                            no_gram_time = time + 1
                        
                        queue.append((ny,nx))
                        visited[ny][nx] = True

bfs()

answer = min(gram_time,no_gram_time)



if answer <= T:
    print(answer)
else:
    print('Fail')
    