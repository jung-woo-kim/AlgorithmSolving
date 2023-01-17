import sys

N = int(sys.stdin.readline().rstrip())

house = []
total = 0

for _ in range(N):
    X,A = map(int,sys.stdin.readline().rstrip().split())

    house.append((X,A))
    total += A

house.sort()

now = 0

for x,a in house:
    now += a

    if now > total//2:
        print(x)
        break