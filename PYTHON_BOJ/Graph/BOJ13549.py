from collections import deque
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

dp = [-1 for _ in range(200001)]

dp[N] = 0

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        now = queue.popleft()

        for i in range(3):
            if i == 0:
                dn = now*2
                if 200000 > dn > -1 and dp[dn] == -1:
                    dp[dn] = dp[now]
                    queue.append(dn)
                elif 200000 > dn > -1 and dp[dn] != -1:
                    if dp[dn] > dp[now]:
                        dp[dn] = dp[now]
            elif i == 1:
                dn = now - 1
                if 200000 > dn > -1 and dp[dn] == -1:
                    dp[dn] = dp[now] + 1
                    queue.append(dn)
                elif 200000 > dn > -1 and dp[dn] != -1:
                    if dp[dn] > dp[now] + 1:
                        dp[dn] = dp[now] + 1
                
            else:
                dn = now + 1
                if 200000 > dn > -1 and dp[dn] == -1:
                    dp[dn] = dp[now] + 1
                    queue.append(dn)
                elif 200000 > dn > -1 and dp[dn] != -1:
                    if dp[dn] > dp[now] + 1:
                        dp[dn] = dp[now] + 1
    

      
            
bfs()
print(dp[K])