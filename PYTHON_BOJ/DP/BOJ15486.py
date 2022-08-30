import sys

N = int(sys.stdin.readline().rstrip())

T = []
P = []

for _ in range(N):
    t,p = map(int,sys.stdin.readline().rstrip().split())
    T.append(t)
    P.append(p)

dp = [0 for i in range(N+1)]


for i in range(N):
    if T[i] <= N - i:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
    
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])
