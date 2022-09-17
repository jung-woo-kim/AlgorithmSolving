from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N+1)]
score = [0 for _ in range(N+1)]
score[0] = 1e9
while True:
    A,B = map(int,sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)
    if A == -1 and B == -1:
        break

def BFS(n):
    q = deque()
    q.append(n)
    q.append(-1)
    visited = [False for _ in range(N+1)]
    visited[n] = True

    num = 0

    while q:
        tmp = q.popleft()
        if tmp == -1:
            if q:
                q.append(-1)
                num += 1
            else:
                return num
        else:
            for node in graph[tmp]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True

for i in range(1,N+1):
    score[i] = BFS(i)

m = min(score)

answer_li = []

for i in range(1,N+1):
    if score[i] == m:
        answer_li.append(i)

print(str(m)+" "+str(len(answer_li)))
print(*answer_li)