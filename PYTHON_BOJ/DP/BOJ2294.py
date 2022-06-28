import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

dp = [0 for _ in range(0,k+1)]
coin = []

for _ in range(0,n):
    coin.append(int(sys.stdin.readline().rstrip()))

for i in range(1, k + 1):
    a = []
    for j in coin:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
print(dp[k])