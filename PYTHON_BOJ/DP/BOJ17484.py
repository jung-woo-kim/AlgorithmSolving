import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(N):
    li = list(map(int,sys.stdin.readline().rstrip().split()))

    board.append(li)

dp = [[[1e9,1e9,1e9]for _ in range(M)]for __ in range(N)]

for x in range(M):
    for i in range(3):
        dp[0][x][i] = board[0][x]

for y in range(1,N):
    for x in range(M):
        if x == 0:
            dp[y][x][1] = dp[y-1][x+1][0] + board[y][x]
            dp[y][x][2] = min(dp[y-1][x][1],dp[y-1][x+1][0]) + board[y][x]
        elif x == M-1:
            dp[y][x][0] = min(dp[y-1][x][1],dp[y-1][x-1][2]) + board[y][x]
            dp[y][x][1] = dp[y-1][x-1][2] + board[y][x]
        else:
            dp[y][x][0] = min(dp[y-1][x][1],dp[y-1][x-1][2]) + board[y][x]
            dp[y][x][1] = min(dp[y-1][x+1][0],dp[y-1][x-1][2]) + board[y][x]
            dp[y][x][2] = min(dp[y-1][x][1],dp[y-1][x+1][0]) + board[y][x]

answer = 1e9

for x in range(M):
    answer = min(min(dp[N-1][x]),answer)
print(answer)
