import sys

C,N = map(int,sys.stdin.readline().rstrip().split())
INF = 1e9
city = []

for _ in range(N):
    cost,costomer = map(int,sys.stdin.readline().rstrip().split())
    city.append((cost,costomer))

dp = [INF] * (C+100)
dp[0] = 0


for c in city:
    for i in range(c[1],C+100):
        dp[i] = min(dp[i],dp[i-c[1]]+c[0])
    

print(min(dp[C:1000]))