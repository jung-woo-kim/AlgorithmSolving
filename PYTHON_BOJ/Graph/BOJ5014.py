from collections import deque
import sys

F,S,G,U,D = map(int,sys.stdin.readline().rstrip().split())

elevator = [[] for _ in range(F+1)]
visited = [False for _ in range(F+1)] 

q = deque()
q.append((S,0))
visited[S] = True

while q:
    n,num = q.popleft()

    if n == G:
        print(num)
        exit()

    u_n = n+U
    d_n = n-D

    if u_n <= F and not visited[u_n]:
        visited[u_n] = True
        q.append((u_n,num+1))
    if d_n > 0 and not visited[d_n]:
        visited[d_n] = True
        q.append((d_n,num+1))

print("use the stairs")