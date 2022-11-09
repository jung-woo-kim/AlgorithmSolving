import sys

T,W = map(int,sys.stdin.readline().rstrip().split())

dp = [[0 for _ in range(W+1)] for __ in range(T)]

for i in range(T):
    tree = int(sys.stdin.readline().rstrip())
    if tree == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1,W+1):
        if j > i+1:
            break
        if tree == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+1
        
        elif tree == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+1
        
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[-1]))