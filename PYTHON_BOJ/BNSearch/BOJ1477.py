import sys

N,M,L = map(int,sys.stdin.readline().split())

rest = list(map(int,sys.stdin.readline().split()))
rest.append(0)
rest.append(L)
rest.sort()

start = 1
end = L-1
result = 0

while start <= end:
    mid = (start + end) // 2
    standard = 0
    cnt = 0
    for i in range(N+2):
        if rest[i] - standard > mid:
            cnt += (rest[i] - standard -1) // mid
        standard = rest[i]

    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)