from collections import deque
import heapq
import queue
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]
queue = []
degree = [0 for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    degree[B] += 1

answer = []

for i in range(1,N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)

    for node in graph[tmp]:
        degree[node] -= 1
        if degree[node] == 0:
            heapq.heappush(queue,node)

    
print(*answer)
