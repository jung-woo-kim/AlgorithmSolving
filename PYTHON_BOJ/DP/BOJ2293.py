import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

dp = [0 for _ in range(0,k+1)]
coin = []

for _ in range(0,n):
    coin.append(int(sys.stdin.readline().rstrip()))

dp[0]=1

for i in coin:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])