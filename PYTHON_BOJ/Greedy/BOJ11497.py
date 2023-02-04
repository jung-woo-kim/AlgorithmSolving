import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    woods = list(map(int,sys.stdin.readline().rstrip().split()))

    woods.sort()
    answer = 0
    answer_li = deque()
    answer_li.append(woods[-1])

    for i in range(len(woods)-2,-1,-1):
        if i % 2 == 0:
            answer_li.append(woods[i])
        else:
            answer_li.appendleft(woods[i])
    
    for i in range(len(woods)-1):
        answer = max(abs(answer_li[i] - answer_li[i+1]),answer)

    answer = max(answer,abs(answer_li[0] - answer_li[-1]))

    print(answer)