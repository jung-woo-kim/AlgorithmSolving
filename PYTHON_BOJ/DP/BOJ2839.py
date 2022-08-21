from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

dp = [0 for i in range(N+6)]

def BFS():
    q = deque()
    q.append((0,0))
    visited = [False for i in range(N+6)]

    while q:
        loc,num = q.popleft()
        if loc == N:
            print(num)
            exit()

        if loc < N+6:
            if not visited[loc]:
                visited[loc] = True
                q.append((loc+3,num+1))
                q.append((loc+5,num+1))

BFS()
print(-1)