import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

woods = list(map(int,sys.stdin.readline().rstrip().split()))

start = 0
end = max(woods)

while end >= start:
    mid = (end + start) // 2
    now = 0

    for w in woods:
        if w - mid > 0:
            now += (w-mid)
    if now == M:
        end = mid
        break
    if now >= M:
        start = mid + 1
    else:
        end = mid -1
        

print(end)