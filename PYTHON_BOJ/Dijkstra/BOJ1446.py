import sys
import heapq

N, D = map(int,sys.stdin.readline().rstrip().split())


graph = [[] for _ in range(D+1)]

for _ in range(N):
    S,E,dist = map(int,sys.stdin.readline().rstrip().split())
    if E > D:
        continue
    graph[S].append((E,dist))

for d in range(D):
    graph[d].append((d+1,1))

distance = [1e9 for _ in range(D+1)]

q = []
heapq.heappush(q,(0,0))
distance[0] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[D])