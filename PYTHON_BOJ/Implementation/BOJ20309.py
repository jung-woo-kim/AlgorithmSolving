import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(N):
    if li[i] % 2 == 0 and i % 2 == 1:
        pass
    elif li[i] % 2 == 1 and i % 2 == 0:
        pass
    else:
        print("NO")
        exit()

print("YES") 