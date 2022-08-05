from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

edge = [[] for _ in range(N+1)]
root = -1
for i in range(1,N+1):
    li = list(map(int,sys.stdin.readline().rstrip().split()))
    if len(li) <= 6:
        root = li[0]
    for j in range(1,len(li),2):
        if li[j] != -1:
            edge[li[0]].append((li[j],li[j+1]))
            edge[li[j]].append((li[0],li[j+1]))
        else:
            break

for i in range(1,N+1):
    edge[i] = list(set(edge[i]))

def BFS(start):
    queue = deque()
    queue.append((start,0))
    visited = [False for _ in range(N+1)]
    visited[start] = True
    max_dist = 0
    max_node = -1
    while queue:
        now,now_dist = queue.popleft()

        for next,dist in edge[now]:
            if not visited[next]:
                visited[next] = True
                queue.append((next,dist+now_dist))
                if max_dist < dist+now_dist:
                    max_dist = dist+now_dist
                    max_node = next
    
    return max_dist,max_node


dist,node = BFS(root)

print(BFS(node)[0])