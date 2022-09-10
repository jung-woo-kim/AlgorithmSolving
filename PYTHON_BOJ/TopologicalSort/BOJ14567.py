from collections import deque
import sys


N,M = map(int,sys.stdin.readline().rstrip().split())

graph =[[] for _ in range(N+1)]
q = deque()
Degree = [0 for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
now = 1

for _ in range(M):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    Degree[B] += 1


for i in range(1,N+1):
    if Degree[i] == 0:
        q.append(i)
        answer[i] = now

q.append(-1)
now += 1

while q:
    tmp = q.popleft()

    if tmp == -1:
        if q:
            now += 1
            q.append(-1)
        else:
            break

    else:
        for node in graph[tmp]:
            Degree[node] -= 1
            if Degree[node] == 0:
                answer[node] = now
                q.append(node)

print(*answer[1:])