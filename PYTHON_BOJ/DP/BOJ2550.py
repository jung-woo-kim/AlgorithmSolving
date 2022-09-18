from bisect import bisect_left
import sys

N = int(sys.stdin.readline().rstrip())
switch = list(map(int,sys.stdin.readline().rstrip().split()))
light = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(N)]

binary = [-1e9]

for i in range(len(switch)):
    idx = light.index(switch[i])
    if binary[-1] < idx:
        binary.append(idx)
        dp[i] = len(binary) -1
    else:
        dp[i] = bisect_left(binary,idx)
        binary[dp[i]] = idx

m = max(dp)
print(m)
answer = []
for i in range(N-1,-1,-1):
    if dp[i] == m:
        m-=1
        answer.append(switch[i])
answer.sort()
print(*answer)
