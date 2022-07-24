from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

graph = [[] for _ in range(101)]

for _ in range(N):
    x, y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)

for _ in range(M):
    u, v = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)

def bfs():
    queue = deque()
    queue.append(1)
    queue.append(-1)
    answer = 0
    while queue:
        n = queue.popleft()
        if n == -1:
            if queue:
                queue.append(-1)
                answer += 1
            else:
                break
        for i in range(1,7):
            dn = n+i
            if dn == 100:
                print(answer+1)
                return
            if dn <= 100:
                if not visited[dn]:
                    
                    if len(graph[dn]) > 0:
                        visited[graph[dn][0]] = True
                        board[graph[dn][0]] = board[n] + 1
                        queue.append(graph[dn][0])
                    else:
                        visited[dn] = True
                        board[dn] = board[n] + 1
                        queue.append(dn)

bfs()
print(board)
