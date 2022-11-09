import sys

N = int(sys.stdin.readline().rstrip())

li = []
answer = 0

for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))


for i in range(N-1,0,-1):
    if(li[i-1] >= li[i]):
        answer += li[i-1] - (li[i]-1)
        li[i-1] = (li[i]-1)
print(answer)