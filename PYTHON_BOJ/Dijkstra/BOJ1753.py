import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        wei,now = heapq.heappop(heap)
        
        for w,next in graph[now]:
            weight = w + wei
            if dp[next] > weight:
                dp[next] = weight
                heapq.heappush(heap,(weight,next))


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])