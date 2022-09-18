import sys

N = int(sys.stdin.readline().rstrip())

time = []

for _ in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    time.append((a,b))

time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

answer = 1
now = time[0][1]

for i in range(1,N):
    if time[i][0] >= now:
        answer += 1
        now = time[i][1]

print(answer)
