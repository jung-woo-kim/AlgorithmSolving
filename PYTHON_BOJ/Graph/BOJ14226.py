import sys
from collections import deque

S = int(sys.stdin.readline().rstrip())

q = deque()
q.append((1,0,0))
visited = [False for _ in range(2001)]

while q:
    now,time,clip = q.popleft()

    if now == S:
        print(time)
        break

    if 0<now<=2000 and not visited[now]:
        visited[now] = True
        q.append((now + clip,time+1,clip))
        q.append((now,time+1,now))
        q.append((now-1,time+1,clip))

