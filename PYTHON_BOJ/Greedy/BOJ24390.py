import sys

time = sys.stdin.readline().rstrip().split(":")
sec = int(time[0]) * 60 + int(time[1])

answer = 0

btn = [600,60,30,10]
check = False
for i in range(4):
    if sec == 0:
        break
    if sec >= btn[i]:
        if i == 2:
            check = True
        answer += (sec//btn[i])
        sec -= (sec//btn[i])*btn[i]

if check:
    print(answer)
else:
    print(answer+1)