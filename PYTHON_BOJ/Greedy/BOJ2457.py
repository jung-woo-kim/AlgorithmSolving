import sys

n = int(sys.stdin.readline())
date = []

# 편의를 위해 100을 곱해 날짜 형식으로 바꿈
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

# 꽃이 피고 지는 날짜를 오름차순으로 정렬 -> 피는 날짜 우선
date.sort(key=lambda x:(x[0], x[1]))

cnt = 0
now_start = 0
now_end = 301

while date:
    if now_end >= 1201 or now_end < date[0][0]:
        break

    for _ in range(len(date)):
        if now_end >= date[0][0]:
            if now_start <= date[0][1]:
                now_start = date[0][1]
            
            date.remove(date[0])
        else:
            break
    
    now_end = now_start
    cnt += 1
        

if now_end < 1201:
    print(0)
else:
    print(cnt)
