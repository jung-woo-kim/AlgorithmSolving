import sys
N, K = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N + 1)]
tmp = []
cnt = 0
for _ in range(N):
    tmp.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    arr[tmp[i][0]] = tmp[i][1:4]

for i in range(1, N+1):
    if arr[i][0] > arr[K][0]:
        cnt += 1
    if arr[i][0] == arr[K][0] and arr[i][1] > arr[K][1]:
        cnt += 1
    if arr[i][0] == arr[K][0] and arr[i][1] == arr[K][1] and arr[i][2] > arr[K][2]:
        cnt += 1

print(cnt + 1)