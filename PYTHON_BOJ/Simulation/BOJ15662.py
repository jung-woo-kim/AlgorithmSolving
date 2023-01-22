import sys

T = int(sys.stdin.readline().rstrip())

topni = []

left_toch_idx = 6
right_toch_idx = 2

for _ in range(T):
    topni.append(list(sys.stdin.readline().rstrip()))

K = int(sys.stdin.readline().rstrip())

def rotate_not_clock(li):
    temp = li[1:]
    temp.append(li[0])
    return temp

def rotate_clock(li):
    temp = li[7:8] + li[0:7]
    return temp

def rotate(li,direction):
    if direction == 1:
        return rotate_clock(li)
    elif direction == -1:
        return rotate_not_clock(li)

for _ in range(K):
    num, direction = map(int,sys.stdin.readline().rstrip().split())

    right_direction = -direction
    left_direction = -direction
    directs = [0] * T
    for i in range(num,T):
        if topni[i-1][right_toch_idx] == topni[i][left_toch_idx]:
            break
        else:
            directs[i] = right_direction
            right_direction = -right_direction

    for i in range(num-2,-1,-1):
        if topni[i+1][left_toch_idx] == topni[i][right_toch_idx]:
            break
        else:
            directs[i] = left_direction
            left_direction = -left_direction

    directs[num-1] = direction

    for i in range(T):
        if directs[i] != 0:
            topni[i] = rotate(topni[i],directs[i])



answer = 0
for li in topni:
    if li[0] == '1':
        answer += 1

print(answer)