import sys

N = int(sys.stdin.readline().rstrip())
li = [1,0,0]

for _ in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())

    temp = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = temp

for i in range(3):
    if li[i] == 1:
        print(i+1)
        break