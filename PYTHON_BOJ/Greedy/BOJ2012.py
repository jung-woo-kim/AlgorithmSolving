import sys

N = int(sys.stdin.readline().rstrip())

expect = []

for _ in range(N):
    expect.append(int(sys.stdin.readline().rstrip()))

expect.sort()

answer = 0

for i in range(1,N+1):
    answer += abs(expect[i-1] - i)

print(answer)