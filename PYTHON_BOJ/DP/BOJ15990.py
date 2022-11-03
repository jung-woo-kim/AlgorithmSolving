import sys

T = int(sys.stdin.readline().rstrip())

num_li = []

for _ in range(T):
    num_li.append(int(sys.stdin.readline().rstrip()))



dp = [[0,0,0] for _ in range(max(num_li))]

dp[0] = ([1,0,0])
dp[1] = ([0,1,0])
dp[2] = ([1,1,1])

for i in range(3,max(num_li)):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for n in num_li:
    print(sum(dp[n-1])% 1000000009)
