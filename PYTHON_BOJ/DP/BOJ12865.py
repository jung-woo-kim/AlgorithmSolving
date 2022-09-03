import sys

wt = []
val = []
N, K = map(int, sys.stdin.readline().strip().split()) 
for i in range(N):
    w, v = map(int, sys.stdin.readline().strip().split())
    wt.append(w) 
    val.append(v)

dp = [[0 for _ in range(K+1)] for __ in range(N+1)]

for i in range(1,N+1):
    for w in range(1,K+1):
        if wt[i-1] <= w:
            dp[i][w] = max(val[i-1] +dp[i-1][w-wt[i-1]],dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[N][K])