import heapq
import sys

n,m,r =  map(int,sys.stdin.readline().rstrip().split())

item = list(map(int,sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int,sys.stdin.readline().rstrip().split())
    edges[a].append((l,b))
    edges[b].append((l,a))


def Dikstra(s):
    item_num = 0

    hq = []
    heapq.heappush(hq,(0,s))

    dp = [1e9 for _ in range(n+1)]
    dp[s] = 0
    while hq:
        w,now = heapq.heappop(hq)

        for next_wei,next in edges[now]:
            weight = w+next_wei
            if dp[next] > weight:
                dp[next] = weight
                heapq.heappush(hq,(weight,next))

    for i in range(1,n+1):
        if dp[i] <= m:
            item_num += item[i-1]
    
    return item_num

answer = 0

for i in range(1,n+1):
    answer = max(answer,Dikstra(i))

print(answer)