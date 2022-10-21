import sys

N,L = map(int,sys.stdin.readline().rstrip().split())
water = list(map(int,sys.stdin.readline().rstrip().split()))
water.sort()

last = 0
answer = 0


for i in range(N):
    if last < water[i]:
        answer += 1
        last = water[i] + L-1
    else:
        pass
print(answer)