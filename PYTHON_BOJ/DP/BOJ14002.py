import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

subsequence = []

order = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == order:
        subsequence.append(arr[i]) 
        order -= 1 

subsequence.reverse()
print(*subsequence)