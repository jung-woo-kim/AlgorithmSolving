import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n,m = map(int,sys.stdin.readline().rstrip().split())
    dp = [[0 for _ in range(m+1)]for __ in range(n)]

    for i in range(m+1):
        dp[0][i] = 1
    
    for y in range(n-1):
        for x in range(1,m+1):
            if dp[y][x] > 0:
                if x*2 < m + 1:
                    for t in range(x*2,m+1):
                        dp[y+1][t] += dp[y][x]

    print(dp)
