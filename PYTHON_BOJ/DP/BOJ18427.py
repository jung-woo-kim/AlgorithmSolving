import sys

N,M,H = map(int,sys.stdin.readline().rstrip().split())

student = []

for _ in range(N):
    student.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp = [[0 for _ in range(H+1)] for __ in range(N+1)]

for i in range(1,N+1):
    for s in student[i-1]:
        dp[i][s] = 1

for i in range(1,N+1):
    for h in range(1,H+1):
        dp[i][h] += dp[i-1][h]
        for s in student[i-1]:
            if h-s > 0:
                dp[i][h] += dp[i-1][h-s]
                
print(dp[-1][-1]%10007)