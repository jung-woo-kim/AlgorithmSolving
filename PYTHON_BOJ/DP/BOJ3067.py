import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = list(map(int,sys.stdin.readline().rstrip().split()))
    money = int(sys.stdin.readline().rstrip())

    dp = [[0 for _ in range(money+1)]for __ in range(N)]
    for i in range(money+1):
        dp[0][i] = 1

    for i in range(1,N):
        for j in range(money+1):
            dp[i][j] += dp[i-1][j]
            if j-coins[i] >= 0:
                dp[i][j] += dp[i-1][j-coins[i]]

    print(dp)  