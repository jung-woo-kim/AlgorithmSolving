import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    dp = [[0,0] for __ in range(n)]
    li1 = list(map(int,sys.stdin.readline().rstrip().split()))
    li2 = list(map(int,sys.stdin.readline().rstrip().split()))

    if n == 1:
        print(max(li1[0],li2[0]))
        continue

    dp[0][0] = li1[0]
    dp[0][1] = li2[0]
    dp[1][0] = dp[0][1] + li1[1]
    dp[1][1] = dp[0][0] + li2[1]

    for i in range(2,n):
        dp[i][0] = max(dp[i-1][1] ,dp[i-2][0] ,dp[i-2][1])+ li1[i]
        dp[i][1] = max(dp[i-1][0] ,dp[i-2][0] ,dp[i-2][1])+ li2[i]
    
    print(max(dp[-1]))