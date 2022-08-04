from collections import deque
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

if N == K:
    print(0)
    print(1)
    exit()

def BFS():
    q = deque()
    q.append(N)
    q.append(-1)

    visited = [0 for _ in range(200001)]
    visited[N] = 0
    check = False
    num = 0
    time = 0

    while q:
        temp = q.popleft()

        if temp == -1:
            
            if check:
                print(time+1)
                print(num)
                return
            else:
                if q:
                    time += 1
                    q.append(-1)

        else:
            now = temp
            if 0 <= now-1 <= 200000 and (visited[now-1] == 0 or visited[now-1] ==time):
                if now-1 == K:
                    check = True
                    num += 1
                else:
                    visited[now-1] = time
                    q.append(now-1)
            
            if 0 <= now+1 <= 200000 and (visited[now+1] == 0 or visited[now+1] ==time):
                if now+1 == K:
                    check = True
                    num += 1
                else:
                    visited[now+1] = time
                    q.append(now+1)

            if 0 <= now*2 <= 200000 and (visited[now*2] == 0 or visited[now*2] ==time):
                if now*2 == K:
                    check = True
                    num += 1
                else:
                    visited[now*2] = time
                    q.append(now*2)


BFS()