import sys

N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().rstrip().split()))

visited = [False for _ in range(N+1)]

dp = [1 for _ in range(N+1)]

for i in range(N):
    if visited[li[i]-1]:
        dp[li[i]] = dp[li[i]-1] + 1
    else:
        dp[li[i]] = 1
    visited[li[i]] = True
print(N-max(dp))