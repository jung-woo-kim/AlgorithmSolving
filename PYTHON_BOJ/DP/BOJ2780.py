import sys

T = int(sys.stdin.readline().rstrip())

dp = [[1 for _ in range(10)] for __ in range(1001)]  

password = [[7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]]

for i in range(1,1001):
    for j in range(10):
        tmp = 0
        for p in password[j]:
            tmp += dp[i-1][p]
        dp[i][j] = tmp
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(sum(dp[N-1])%1234567)