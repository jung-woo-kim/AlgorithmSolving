import sys

N = int(sys.stdin.readline().rstrip())

dp = [[[0,0,0,0,0,0,0,0,0,0] for __ in range(10)] for _ in range(N+1)]

for i in range(1,10):
    dp[1][i][i] = 1

for i in range(2,N+1):
    for j in range(10):
        if j-1 >= 0:
            for k in range(10):
                dp[i][j][k] += dp[i-1][j-1][k]
        if j+1 < 10:
            for k in range(10):
                dp[i][j][k] += dp[i-1][j+1][k]

print(dp)