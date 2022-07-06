import sys

N = int(sys.stdin.readline().rstrip())

li = [0]

dp = [0 for _ in range(N+1)]

for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))

dp[1] = li[1]

if N == 1:
    print(dp[1])
    exit()

dp[2] = li[1] + li[2]

if N == 2:
    print(dp[2])
    exit()

for i in range(3,N+1):
    dp[i] = max(dp[i - 1], dp[i - 3] + li[i - 1] + li[i], dp[i - 2] + li[i])


print(dp)