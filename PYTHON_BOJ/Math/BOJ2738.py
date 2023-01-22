import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip().split())))

for _ in range(N):
    B.append(list(map(int,sys.stdin.readline().rstrip().split())))

C = []

for y in range(N):
    row = []
    for x in range(M):
        row.append(A[y][x] + B[y][x])
    C.append(row)

for y in range(N):
    print(*C[y])