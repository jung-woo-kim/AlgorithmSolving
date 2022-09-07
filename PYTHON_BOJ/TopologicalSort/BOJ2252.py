from collections import deque
import queue
import sys


N,M = map(int,sys.stdin.readline().rstrip().split())

graph = [[]for _ in range(N+1)]
queue = deque()
degree = [0 for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    degree[B] += 1

for i in range(1,N+1):
    if degree[i] == 0:
        queue.append(i)
answer = []
while queue:
    tmp = queue.popleft()
    answer.append(tmp)

    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

print(*answer)
