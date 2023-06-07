from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(sx,sy,maps,visited):
    q = deque()
    q.append([sx,sy])
    visited[sx][sy] = True
    ans = int(maps[sx][sy])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != "X":
                    q.append([nx,ny])
                    ans += int(maps[nx][ny])
                    visited[nx][ny] = True
                
    return ans

def solution(maps):
    answer = []

    visited = [[False for _ in range(len(maps[0]))] for __ in range(len(maps))]

    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] != "X" and not visited[x][y]:
                answer.append(BFS(x,y,maps,visited))
    if len(answer) == 0:
        answer.append(-1)
   
    answer.sort()
    return answer

solution(["X591X","X1X5X","X231X", "1XXX1"])