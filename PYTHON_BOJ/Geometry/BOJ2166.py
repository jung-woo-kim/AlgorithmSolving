import sys

N = int(sys.stdin.readline().rstrip())

li = []

for _ in range(N):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    li.append((x,y))

li.append(li[0])

temp1 = 0

for i in range(N):
    temp1 += (li[i][0] * li[i+1][1])

temp2 = 0

for i in range(1,N+1):
    temp2 += (li[i][0] * li[i-1][1])

print(abs(temp1 - temp2) * 0.5)
