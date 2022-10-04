import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

memo = dict()
now = 0
for _ in range(N):
    memo[sys.stdin.readline().rstrip()] = 1
    now += 1

for _ in range(M):
    li = sys.stdin.readline().rstrip().split(',')

    for st in li:
        try:
            if memo[st] == 1:
                memo[st] = 0
                now -= 1
        except:
            pass
    print(now)