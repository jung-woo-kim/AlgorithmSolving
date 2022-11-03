import sys

T = int(sys.stdin.readline().rstrip())

num_li = []

for _ in range(T):
    num_li.append(int(sys.stdin.readline().rstrip()))

dp = [0 for _ in range(max(num_li))]

dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3,max(num_li)):
    dp[i] = (dp[i-3] + dp[i-2] +dp[i-1]) % 1000000009

for n in num_li:
    print(dp[n-1])