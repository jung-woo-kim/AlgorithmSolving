import sys

N,C = map(int,sys.stdin.readline().rstrip().split())

house = []

for i in range(N):
    house.append(int(sys.stdin.readline().rstrip()))

house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (end + start) // 2

    cnt = 1
    standard = 0

    for i in range(N):
        if house[i] - house[standard] >= mid:
            cnt += 1
            standard = i

    if cnt < C:
        end = mid-1
    else:
        start = mid + 1
    
print(end)
