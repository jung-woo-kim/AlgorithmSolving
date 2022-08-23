from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)]for __ in range(N)]

dp[0][0] = 1
for y in range(N):
    for x in range(N):
        if y == N-1 and x == N-1:
            break
        if 0 <= y+board[y][x] < N:
            dp[y+board[y][x]][x] += dp[y][x]
        if 0 <=x+board[y][x] < N:
            dp[y][x+board[y][x]] += dp[y][x]
        
print(dp[-1][-1])
