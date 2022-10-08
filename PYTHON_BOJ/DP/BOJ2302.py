import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

vip = [int(sys.stdin.readline()) for _ in range(M)]



dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1



for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1

if M > 0:
    pre = 0

    for j in range(M):
        answer *= dp[vip[j] - 1 - pre]
        pre = vip[j]
    answer *= dp[N - pre]
else:
    answer = dp[N]
print(answer)