from collections import deque
import sys


T = int(sys.stdin.readline().rstrip())

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]

answer = []

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    night = list(map(int,sys.stdin.readline().rstrip().split()))
    goal = list(map(int,sys.stdin.readline().rstrip().split()))

    visited = [[False for _ in range(N)] for _ in range(N)]
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if night[0] == goal[0] and night[1] == goal[1]:
        answer.append(0)
        continue

    queue =deque()
    queue.append([night[1],night[0]])
    board[night[1]][night[0]] = 0
    visited[night[1]][night[0]] = True
    result = 0
    while queue:
        #y,x
        check = False
        now = queue.popleft()
        for i in range(0,8):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < N:
                if not visited[ny][nx]:
                    board[ny][nx] = board[now[0]][now[1]] + 1
                    if ny == goal[1] and nx == goal[0]:
                        result = board[ny][nx]
                        answer.append(result)
                        check = True
                    visited[ny][nx] = True
                    
                    queue.append([ny,nx])
        if check:
            break

for a in answer:
    print(a)    


