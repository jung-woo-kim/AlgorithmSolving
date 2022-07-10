import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

listen = dict()

for _ in range(N):
    listen[sys.stdin.readline().rstrip()] = 0

for _ in range(M):
    try:
        listen[sys.stdin.readline().rstrip()] += 1
    except:
        pass

듣보잡 = []

for key in listen.keys():
    if listen[key] > 0:
        듣보잡.append(key)

print(len(듣보잡))
듣보잡.sort()
for item in 듣보잡:
    print(item)