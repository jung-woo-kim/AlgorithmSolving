import sys

N ,M = map(int,sys.stdin.readline().rstrip().split())

bosuck = []

for _ in range(M):
    bosuck.append(int(sys.stdin.readline().rstrip()))

end = max(bosuck)
start = 1
answer = 1e9

while end >= start:
    mid = (end+start) // 2

    # temp는 질투심이 mid일 때 인원 수
    temp = 0
    for b in bosuck:
        temp += (b // mid)
        if b % mid != 0:
            temp += 1
    
    # 더 크면 불가능 
    if temp > N:
        start = mid + 1
    else:
        end = mid - 1
        answer = min(answer,mid)

print(answer)