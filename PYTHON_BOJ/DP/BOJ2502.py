import sys

D, K = map(int,sys.stdin.readline().rstrip().split())

dp = [0 for _ in range(D+1)]

dp[1] = 1
dp[2] = 1

while True:
    for i in range(3,D+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    if dp[D] == K:
        break

    if dp[D] > K:
        dp[1] += 1
        dp[2] = dp[1]
    
    if dp[D] < K:
        dp[2] += 1

print(dp[1])
print(dp[2])