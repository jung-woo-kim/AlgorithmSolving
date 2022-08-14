from bisect import bisect, bisect_left
import sys

N = int(sys.stdin.readline().rstrip())

pole = []

for _ in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    pole.append((a,b))

pole.sort()
binary = [-1]

dp = [0 for _ in range(N)]

for i in range(N):
    if pole[i][1] > binary[-1]:
        binary.append(pole[i][1])
        dp[i] = len(binary) - 1
    else:
        dp[i] = bisect_left(binary,pole[i][1])
        binary[dp[i]] = pole[i][1]

max_connect = max(dp)

answer = []

for i in range(N-1,-1,-1):
    if dp[i] == max_connect:
        max_connect -= 1
    else:
        answer.append(pole[i][0])

answer.reverse()
print(len(answer))
for a in answer:
    print(a)