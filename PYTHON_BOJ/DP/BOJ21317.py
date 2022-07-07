import sys

N = int(sys.stdin.readline())

stone = []
stone.append((0,0))
result = 1e9

for _ in range(N-1):
    s,b = map(int,sys.stdin.readline().split())
    stone.append((s,b))



K = int(sys.stdin.readline())

for j in range(1,N):
    dp = [0 for _ in range(N+2)]
    dp[2] = stone[1][0]
    for i in range(3,N+1):
        #k가 j 위치에 있으면
        if j == i-3:
            dp[i] = min(dp[i-1] + stone[i-1][0],dp[i-2] + stone[i-2][1],dp[i-3]+K)
        else:
            dp[i] = min(dp[i-1] + stone[i-1][0],dp[i-2] + stone[i-2][1])
    result = min(result,dp[N])

if N == 1:
    result = 0
print(result)