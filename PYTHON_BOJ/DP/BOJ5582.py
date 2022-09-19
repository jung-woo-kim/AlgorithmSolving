import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()


dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
answer = 0
for b in range(1,len(B)+1):
    for a in range(1,len(A)+1):
        if A[a-1] == B[b-1]:
            dp[b][a] = dp[b-1][a-1]+1
    answer = max(answer,max(dp[b]))
print(answer)