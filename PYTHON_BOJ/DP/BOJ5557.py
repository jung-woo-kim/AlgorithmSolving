import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [[0 for _ in range(21)] for __ in range(N-1)]

if 0<= li[0] <= 20: 
    dp[0][li[0]] = 1
else:
    print(0)
    exit()

for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j] > 0:
            if 0<= j - li[i] <= 20:
                dp[i][j - li[i]] += dp[i-1][j]
            if 0<= j + li[i] <= 20:
                dp[i][j + li[i]] += dp[i-1][j]

print(dp[N-2][li[-1]])
