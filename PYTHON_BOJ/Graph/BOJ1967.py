from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,sys.stdin.readline().rstrip().split())
    edges[a].append((b,c))
    edges[b].append((a,c))


def BFS(start):
    queue = deque()
    queue.append((start,0))
    visited = [False for _ in range(N+1)]
    visited[start] = True
    max_dist = 0
    max_node = -1

    while queue:
        now,now_dist = queue.popleft()

        for next,dist in edges[now]:
            if not visited[next]:
                if max_dist < now_dist+dist:
                    max_dist = now_dist+dist
                    max_node = next
                visited[next] = True
                queue.append((next,now_dist+dist))
    return max_dist,max_node

if N == 1:
    print(0)
else:
    dist,node = BFS(1)
    print(BFS(node)[0])