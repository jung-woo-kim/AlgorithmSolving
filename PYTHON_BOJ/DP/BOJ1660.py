import sys

N = int(sys.stdin.readline().rstrip())
ball = [1]
for i in range(2,121):
    ball.append(ball[-1]+i)

for i in range(1,120):
    ball[i] = ball[i]+ball[i-1]

dp = [1e9 for _ in range(N+1)]

for i in range(1,N+1):
    for j in ball:
        if j == i:
            dp[i] = 1
            break
        if j > i:
            break
        
        dp[i] = min(dp[i],dp[i-j] + 1)

print(dp[N])
