from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def L_BFS(maps,sx,sy):
    s_visited = [[False for _ in range(len(maps[0]))]for __ in range(len(maps))]
    s_visited[sx][sy] = True
    q = deque()
    q.append([0,sx,sy])

    while q:
        time,x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if not s_visited[nx][ny] and maps[nx][ny] != "X":
                    if maps[nx][ny] == "L":
                        return time+1,nx,ny
                    else:
                        q.append([time+1,nx,ny])
                        s_visited[nx][ny] = True
    return -1,-1,-1
def E_BFS(maps,sx,sy,time):
    visited = [[False for _ in range(len(maps[0]))]for __ in range(len(maps))]
    visited[sx][sy] = True
    q = deque()
    q.append([time,sx,sy])
    while q:
        time,x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != "X":
                        if maps[nx][ny] == "E":
                            return time+1
                        else:
                            q.append([time+1,nx,ny])
                            visited[nx][ny] = True
            
    return -1


def solution(maps):
    answer = 0

    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == "S":
                sx,sy = x,y
            if maps[x][y] == "E":
                gx,gy = x,y
    time,x,y = L_BFS(maps,sx,sy)

    if time == -1:
        return -1
    
    return E_BFS(maps,x,y,time)

solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])