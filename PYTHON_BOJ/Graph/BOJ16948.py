import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

sr,sc,gr,gc = map(int,sys.stdin.readline().rstrip().split())

dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]

visited = [[False for _ in range(N)] for __ in range(N)]

q = deque()
q.append((sr,sc,0))
visited[sr][sc] = True

while q:
    r,c,now = q.popleft()
    
    if r == gr and c == gc:
        print(now)
        exit()
    
    for i in range(6):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr,nc,now+1))

print(-1)