import sys

N = int(sys.stdin.readline().rstrip())

honey = list(map(int,sys.stdin.readline().rstrip().split())) 

answer = 0

house_idx = 0
bee1 = N-1

s = [0 for _ in range(0,N+1)]

for i in range(1,N+1):
    s[i] =s[i-1] + honey[i-1]

print(s)

if N == 3:
    answer = max(honey) * 2
    print(answer)
    exit()

if honey[house_idx] < honey[N-1]:
    house_idx = N-1
    bee1 = 0



