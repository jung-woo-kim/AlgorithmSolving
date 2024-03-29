import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m, t = map(int,sys.stdin.readline().rstrip().split())
    s, g, h = map(int,sys.stdin.readline().rstrip().split())

    edge = [[] for n in range(n+1)]

    goal = []
    for __ in range(m):
        a,b,d = map(int,sys.stdin.readline().rstrip().split())
        edge[a].append((d,b))
        edge[b].append((d,a))
    
    for __ in range(t):
        x = int(sys.stdin.readline().rstrip())
        goal.append(x)

    goal.sort()

    def Dijkstra(start,dp):
        hq = []
        heapq.heappush(hq,(0,start))
        dp[start] = 0
        while hq:
            now_w,now_node = heapq.heappop(hq)

            if dp[now_node] < now_w:
                continue

            for next_w,next_node in edge[now_node]:
                if dp[next_node] > now_w + next_w:
                    dp[next_node] = now_w + next_w
                  
                    heapq.heappush(hq,(now_w + next_w,next_node))


    
    dp_first = [sys.maxsize for _ in range(n+1)]
    Dijkstra(s,dp_first)
    temp = ""
    if dp_first[g] < dp_first[h]:
        dp = [sys.maxsize for _ in range(n+1)]
        Dijkstra(h,dp)
        for i in range(len(goal)):
            if dp_first[goal[i]] == dp_first[h] + dp[goal[i]]:
                temp += str(goal[i]) + " "
    
    else:
        dp = [sys.maxsize for _ in range(n+1)]
        Dijkstra(g,dp)
        for i in range(len(goal)):
            if dp_first[goal[i]] == dp_first[g] + dp[goal[i]]:
                temp += str(goal[i]) + " "


    print(temp)
    