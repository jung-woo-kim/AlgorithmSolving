import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

r,c,d = map(int,sys.stdin.readline().rstrip().split())

dx = [0,1,0,-1]
dy = [-1,0,1,0]

##청소한 구역 2 / 빈칸 0 / 벽 1
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

board[r][c] = 3
answer = 1
check = 0
while True:

    board[r][c] = 2
    d = (d-1) % 4

    nc = c + dx[d]
    nr = r + dy[d]

    if board[nr][nc] == 0:
        r = nr
        c = nc
        answer += 1
        check = 0
        continue
    else:
        check += 1
        if check == 4:
            check = 0
            nc = c - dx[d]
            nr = r - dy[d]
            if board[nr][nc] == 1:
                break
            else:
                r = nr
                c = nc


print(answer)