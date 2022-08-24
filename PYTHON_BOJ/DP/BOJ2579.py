import sys

N = int(sys.stdin.readline().rstrip())

li = [0]

for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))

dp = [0 for _ in range(N+1)]



if N == 1:
    print(li[1])
    exit()

if N == 2:
    print(li[1] + li[2])
    exit()

if N == 3:
    print(max(li[1] + li[3],li[3] + li[2]))
    exit()

dp[1] = li[1]
dp[2] = li[1] + li[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-2]+li[i],dp[i-3]+li[i-1]+li[i])

print(dp)

