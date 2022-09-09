from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N,K = map(int,sys.stdin.readline().rstrip().split())

    time = [0 for __ in range(N+1)]
    li = list(map(int,sys.stdin.readline().rstrip().split()))
    graph = [[] for __ in range(N+1)]
    degree = [0 for __ in range(N+1)]
    dp = [0 for __ in range(N+1)]

    q = deque()

    for i in range(1,N+1):
        time[i] = li[i-1]
    
    for __ in range(K):
        X,Y = map(int,sys.stdin.readline().rstrip().split())
        graph[X].append(Y)
        degree[Y] += 1
    
    for i in range(1,N+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        tmp = q.popleft()

        for node in graph[tmp]:
            degree[node] -= 1
            dp[node] = max(dp[tmp] + time[node],dp[node])
            if degree[node] == 0:
                q.append(node)

    print(dp[int(sys.stdin.readline().rstrip())])