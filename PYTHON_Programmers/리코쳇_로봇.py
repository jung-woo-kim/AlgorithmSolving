
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(sx,sy,visited,board):
    q = deque([])
    q.append([0,sx,sy])
    visited[sx][sy] = True
    while q:
        time,x,y = q.popleft()
        
        if board[x][y] == "G":
            return time
        for i in range(4):
            if dx[i] == 0:
                ny = y
                
                while True:
                    ny += dy[i]
                    
                    if ny >= len(board[0]):
                        ny = ny - 1
                        break
                    if ny < 0:
                        ny = 0
                        break

                    if board[x][ny] == "D":
                        if dy[i] == 1:
                            ny = ny -1
                        else:
                            ny = ny +1
                        
                        break
                if not visited[x][ny]:
                    q.append([time+1,x,ny])
                    visited[x][ny] = True
                    
                
            if dy[i] == 0:
                nx = x
                while True:
                    nx += dx[i]
                    
                    if nx >= len(board):
                        nx = nx -1
                        break

                    if nx < 0:
                        nx = 0
                        break
                    if board[nx][y] == "D":
                        if dx[i] == 1:
                            nx = nx -1
                        else:
                            nx = nx +1
                        break
                if not visited[nx][y]:
                    q.append([time+1,nx,y])
                    visited[nx][y] = True
                    
    return -1

            
def solution(board):

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "R":
                sx,sy = x,y
    visited = [[False for _ in range(len(board[0]))] for __ in range(len(board))]

    return BFS(sx,sy,visited,board)

solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])