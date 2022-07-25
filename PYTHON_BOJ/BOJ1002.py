import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().rstrip().split())
    r = r1 + r2
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dist == r:
        print(1)
    elif dist > r:
        print(0)
    elif dist < abs(r1-r2):
        print(0)
    elif dist == abs(r1-r2):
        print(1)
    else:
        print(2)

    