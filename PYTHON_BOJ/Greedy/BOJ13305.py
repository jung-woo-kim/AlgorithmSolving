import sys

N = int(sys.stdin.readline().rstrip())

distance = list(map(int,sys.stdin.readline().rstrip().split()))
price =list(map(int,sys.stdin.readline().rstrip().split()))

np = price[0]
answer = 0
for i in range(len(distance)):
    answer += np*distance[i]
    if price[i+1] < np:
        np = price[i+1]

print(answer)