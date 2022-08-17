from collections import deque
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited_island = [[False for _ in range(M)] for __ in range(N)]
visited_bridge = [[False for _ in range(M)] for __ in range(N)]

island_num = 0

edges = []

def BFS(sy,sx,island_num):
    q = deque()
    q.append((sy,sx))
    visited_island[sy][sx] = True
    board[sy][sx] = island_num
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0<= nx <M and not visited_island[ny][nx] and board[ny][nx] != 0:
                visited_island[ny][nx] = True
                board[ny][nx] = island_num
                q.append((ny,nx))

def BFS_make_bridge(sy,sx):
    q = deque()
    q.append((sy,sx))
    visited_bridge[sy][sx] = True
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0<= nx <M and not visited_bridge[ny][nx]:
                if board[ny][nx] != 0:
                    visited_bridge[ny][nx] = True
                    q.append((ny,nx))

                if board[ny][nx] == 0:
                    ty = ny + dy[i]
                    tx = nx + dx[i]
                    length = 1
                    while 0 <= ty < N and 0<= tx <M:
                        if board[ty][tx] != 0:
                            if length>1:
                                edges.append((length, board[ny-dy[i]][nx-dx[i]],board[ty][tx]))
                            break
                        ty += dy[i]
                        tx += dx[i]
                        length += 1

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for y in range(N):
    for x in range(M):
        if not visited_island[y][x] and board[y][x] != 0:
            island_num += 1
            BFS(y,x,island_num)

for y in range(N):
    for x in range(M):
        if not visited_bridge[y][x] and board[y][x] != 0:
            BFS_make_bridge(y,x)

parent = [i for i in range(island_num+1)]

edges.sort()
answer = 0

for w,a,b in edges:
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        if a_parent<b_parent:
            parent[b_parent] = a_parent
        else: 
            parent[a_parent] = b_parent
        answer += w
    

for i in range(1,len(parent)):
    if find(i) != 1:
        print(-1)
        exit()

if answer == 0:
    print(-1)
else:
    print(answer)