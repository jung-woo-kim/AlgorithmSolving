import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1e9 for _ in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(1,li[i]+1):
        if i+j < N:
            dp[i + j] = min(dp[i]+1,dp[i + j])
if dp[N-1] == 1e9:
    print(-1)
else:
    print(dp[N-1])