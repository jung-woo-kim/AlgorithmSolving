import sys

N,M,K = map(int,sys.stdin.readline().split())

essential_x = (K-1) % M
essential_y = (K-1) // M


if K==0:
    essential_x = 0
    essential_y = 0

dp = [[0 for _ in range(M)] for __ in range(N)]
dp[0][0] = 1
for y in range(essential_y+1):
    for x in range(essential_x+1):
        if y - 1 >= 0:
            dp[y][x] += dp[y-1][x]
        if x - 1 >= 0:
            dp[y][x] += dp[y][x-1]

check = False    
for y in range(essential_y,N):
    for x in range(essential_x,M):
        if check:
            if y - 1 >= 0:
                dp[y][x] += dp[y-1][x]
            if x - 1 >= 0:
                dp[y][x] += dp[y][x-1]
        check = True
print(dp[-1][-1])
