import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

lecture = list(map(int,sys.stdin.readline().rstrip().split()))

blue = sum(lecture)

if M == 1:
    print(blue)
    exit()
start = 0
end = blue
res = blue

while end >= start:
    mid = (start + end) // 2

    # 블루레이 개수
    num = 1
    # 블루레이의 현재 길이
    now = 0
    idx = 0

    if max(lecture) > mid:
        start = mid + 1
        continue

    for i in range(len(lecture)):
        # 이전 값이랑 지금 값 더해서 mid 보다 작으면 계속 더해준다
        if now + lecture[i] <= mid:
            now += lecture[i]
        # mid 보다 커지면 현재 data[i]가 tmp 로 들어가고
        # 전에 있던 tmp는 0 초기화 해주고 개수 1개 늘려준다.
        else:
            now = lecture[i]
            num += 1

    if num <= M:
        end = mid -1
        res = min(mid,res)
    else:
        start = mid + 1


print(res)