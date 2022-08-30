import sys

N,S,M = map(int,sys.stdin.readline().rstrip().split())

songs = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [[0 for __ in range(M+1)] for _ in range(N+1)]

dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j+songs[i] <= M:
                dp[i+1][j+songs[i]] = 1
            if j-songs[i] >= 0:
                dp[i+1][j-songs[i]] = 1

ans = -1

for i in range(M, -1, -1):
    if dp[N][i]==1:
        ans = i
        break
print(ans)
