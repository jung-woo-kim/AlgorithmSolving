import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

dp = [["" for _ in range(len(b)+1)] for __ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+a[i-1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[len(a)][len(b)]))
print(dp[len(a)][len(b)])