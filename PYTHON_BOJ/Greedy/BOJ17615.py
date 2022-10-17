import sys

N = int(sys.stdin.readline().rstrip())
ball = sys.stdin.readline().rstrip()

tmp = ball[-1]

change_idx = -1

for i in range(N-2,-1,-1):
    if ball[i] != tmp:
        change_idx = i
        break

if change_idx == -1:
    print(0)
else:
    st = ball[0:change_idx+1]
    red = 0
    blue = 0
    for i in range(len(st)):
        if st[i] == "R":
            red += 1
        else:
            blue += 1
    print(min(red,blue))