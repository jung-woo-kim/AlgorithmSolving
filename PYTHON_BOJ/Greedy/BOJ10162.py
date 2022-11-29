import sys

five_minute = 0
one_minute = 0
ten_second = 0

T = int(sys.stdin.readline().rstrip())

while True:
    if T - 300 >= 0:
        T -= 300
        five_minute += 1
    else:
        break

while True:
    if T - 60 >= 0:
        T -= 60
        one_minute += 1
    else:
        break

while True:
    if T - 10 >= 0:
        T -= 10
        ten_second += 1
    else:
        break

if T != 0:
    print(-1)
else:
    print(str(five_minute) + " " + str(one_minute) + " " + str(ten_second))

