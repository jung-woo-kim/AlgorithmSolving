from copy import copy
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

    

    def Dijkstra(start):
        hq = []
        heapq.heappush(hq,(0,start,[start]))
        dp[start] = [0,[]]
        while hq:
            now_w,now_node,route = heapq.heappop(hq)

            if dp[now_node][0] < now_w:
                continue

            for next_w,next_node in edge[now_node]:
                if dp[next_node][0] > now_w + next_w:
                    dp[next_node][0] = now_w + next_w
                    temp = []
                    temp = copy(route)
                    temp.append(next_node)

                    dp[next_node][1] = temp
                  
                    heapq.heappush(hq,(now_w + next_w,next_node,temp))

    answer = []
    dp = [[1e9,[]] for _ in range(n+1)]
    Dijkstra(s)
    print(dp)
    # for i in range(len(goal)):
        
    #     route = 
    #     for j in range(len(route)-1):
    #         if route[j] == g and route[j+1] == h:
    #             answer.append(goal[i])
    #             break
    #         if route[j+1] == g and route[j] == h:
    #             answer.append(goal[i])
    #             break 
    # answer.sort()

    # temp = ""
    # for a in answer:
    #     temp += str(a)+" "
    # print(temp)