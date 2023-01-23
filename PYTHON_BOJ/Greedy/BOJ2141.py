import sys

N = int(sys.stdin.readline().rstrip())

office = []

mid = 0

for _ in range(N):
    X,A = map(int,sys.stdin.readline().rstrip().split())
    office.append((X,A))
    mid += A

mid = mid / 2

office.sort()

total = 0

for i in range(N):
    total += office[i][1]

    if total >= mid:
        print(office[i][0])
        break