from copy import copy
import heapq
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

bus = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    bus[a].append((c,b))


start,end = map(int,sys.stdin.readline().rstrip().split())

dp = [sys.maxsize for _ in range(N+1)]

def Dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start,[start]))
    answer_route = []

    while hq:
        now_w,now_node,route = heapq.heappop(hq)

        if dp[now_node] < now_w:
            continue

        for next_w,next_node in bus[now_node]:
            if dp[next_node] > now_w + next_w:
                dp[next_node] = now_w + next_w
                temp = []
                temp = copy(route)
                temp.append(next_node)
                if next_node == end:
                    answer_route = temp
                heapq.heappush(hq,(now_w + next_w,next_node,temp))

    return answer_route

answer = Dijkstra(start)
print(dp[end])
print(len(answer))
temp = ""
for a in answer:
    temp += str(a)+" "
print(temp)

