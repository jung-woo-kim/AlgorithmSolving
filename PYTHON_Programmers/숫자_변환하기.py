from collections import deque

def solution(x, y, n):
    answer = -1
    q = deque()
    q.append([0,x])
    visited = [False for _ in range(y+1)]
    while q:
        time,loc = q.popleft()

        if loc == y:
            return time + 1
        for i in range(3):
            if i == 0:
                nx = loc + n
            if i == 1:
                nx = loc * 2
            if i == 2:
                nx = loc * 3
        
        if nx <= y and not visited[nx]:
            q.append([time+1,nx])
            visited[nx] = True

    return answer