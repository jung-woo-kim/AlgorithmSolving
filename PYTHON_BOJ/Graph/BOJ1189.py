import sys

R,C,K = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(R):
    board.append(sys.stdin.readline().rstrip())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0
visited = [[False for _ in range(C)]for __ in range(R)]
visited[R-1][0] = True

def DFS(y,x,depth):
    global answer
    if depth == K:
        if y == 0 and x == C-1:
            answer += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=ny<R and 0<=nx<C:
            if board[ny][nx] != "T":
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    DFS(ny,nx,depth+1)
                    visited[ny][nx] = False

DFS(R-1,0,1)

print(answer)