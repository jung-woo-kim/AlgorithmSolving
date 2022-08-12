from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

def BFS():
    q = deque()
    q.append((N,str(N)))
    q.append(-1)
    visited = [False for _ in range(100001)]
    visited[N] = True
    num = 0

    while q:
        temp = q.popleft()
        if temp == -1:
            if q:
                q.append(-1)
                num += 1
            else:
                return
        else:
            now, route = temp

            if now == M:
                print(num)
                print(route)
                return


            if 0 <= now+1 < 100001 and not visited[now+1]:
                visited[now+1] = True
                r = route
                r += " "+str(now+1)
                q.append((now+1,r))
            
            if 0 <= now-1 < 100001 and not visited[now-1]:
                visited[now-1] = True
                r = route
                r += " "+str(now-1)
                q.append((now-1,r))
            
            if 0 <= now*2 < 100001 and not visited[now*2]:
                visited[now*2] = True
                r = route
                r += " "+str(now*2)
                q.append((now*2,r))


BFS()