from bisect import bisect_left
import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(N)]
binary = [-1000000001]

for i in range(N):
    if binary[-1] < arr[i]:
        binary.append(arr[i])
        dp[i] = len(binary)-1
    else:
        dp[i] = bisect_left(binary,arr[i])
        binary[dp[i]] = arr[i]

maxLen = max(dp)

print(maxLen)
answer = []
for i in range(N-1,-1,-1):
    if dp[i] == maxLen:
        answer.append(arr[i])
        maxLen-=1

answer.reverse()
print(*answer)