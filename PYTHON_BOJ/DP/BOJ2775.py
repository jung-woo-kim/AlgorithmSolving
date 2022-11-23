import sys

T = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(14)] for __ in range(15)]

for i in range(1,15):
    dp[0][i-1] = i
    dp[i][0] = 1

for i in range(1,15):
    for j in range(1,14):
        dp[i][j] = dp[i][j-1]+ dp[i-1][j]


for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())

    print(dp[K][N-1])
