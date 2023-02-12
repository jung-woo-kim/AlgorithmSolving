import sys

T = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(10)] for _ in range(1001)]
dp[0] = [1 for _ in range(10)]

# 끝 자리수가 0인 것의 개수
# 1인 것의 개수
# ...

for i in range(1,1001):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(sum(dp[N-1]))