from bisect import bisect_left
import sys

N = int(sys.stdin.readline().rstrip())

edges = []

for _ in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    edges.append((a,b))

edges.sort()
binary = [0]
dp = [0 for i in range(N)]

answer = 0

for i in range(N):
    if edges[i][1] > binary[-1]:
        binary.append(edges[i][1])
        dp[i] = len(binary) -1
    else:
        dp[i] = bisect_left(binary,edges[i][1])
        binary[dp[i]] = edges[i][1]   
print(N-max(dp))