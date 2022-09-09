from collections import deque
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

degree = [0 for _ in range(N+1)]
q = deque()
graph = [[] for _ in range(N+1)]

for _ in range(M):
    li = list(map(int,sys.stdin.readline().rstrip().split()))

    for i in range(1,len(li)-1):
        graph[li[i]].append(li[i+1])
        degree[li[i+1]] += 1

answer = []

for i in range(1,N+1):
    if degree[i] == 0:
        q.append(i)
        answer.append(i)


while q:
    tmp = q.popleft()
    
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
            answer.append(i)
    

if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)
    