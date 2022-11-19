import sys
from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def BFS(start,end,visited):
    q = deque()
    q.append((start,0))
    visited[start[0]][start[1]][start[2]] = True
    while q:
        now, time = q.popleft()
        if now[0] == end[0] and now[1] == end[1] and now[2] == end[2]:
            return time
        for i in range(6):
            nz = now[0] + dz[i]
            ny = now[1] + dy[i]
            nx = now[2] + dx[i]

            if 0<=nz<L and 0<=ny<R and 0<=nx<C and not visited[nz][ny][nx]:
                if building[nz][ny][nx] != '#':
                    visited[nz][ny][nx] = True
                    q.append(((nz,ny,nx),time+1))
    return -1
while True:
    L,R,C = map(int,sys.stdin.readline().rstrip().split())

    if L == 0 and R == 0 and C == 0:
        break
    building = []
    
    for _ in range(L):
        floor = []
        for __ in range(R):
            floor.append(sys.stdin.readline().rstrip())
        building.append(floor)
        sys.stdin.readline().rstrip()
    
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if building[z][y][x] == 'S':
                    start = (z,y,x)
                if building[z][y][x] == 'E':
                    end = (z,y,x)
    
    visited = [[[False for _ in range(C)] for __ in range(R)] for ___ in range(C)]

    answer = BFS(start,end,visited)

    if answer == -1:
        print("Trapped!")
    else:
        print("Escaped in "+str(answer)+" minute(s).")