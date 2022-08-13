from bisect import bisect_left
import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(N)]

binary = [-1000001]

for i in range(N):
    if arr[i] > binary[-1]:
        binary.append(arr[i])
        dp[i] = len(binary) -1
    else:
        dp[i] = bisect_left(binary,arr[i])
        binary[dp[i]] = arr[i]
    
print(max(dp))