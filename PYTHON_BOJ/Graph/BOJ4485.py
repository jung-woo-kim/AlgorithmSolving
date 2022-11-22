import sys
import heapq

dx = [1,0,-1,0]
dy = [0,1,0,-1]

problem = 1

while True:
    N = int(sys.stdin.readline().rstrip())
    
    if N == 0:
        break

    board = []
    for _ in range(N):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    hq = []
    heapq.heappush(hq,(board[0][0],(0,0)))
    visited = [[1e9 for __ in range(N)] for _ in range(N)]
    visited[0][0] = board[0][0]
    while hq:
        now,positon = heapq.heappop(hq)

        for i in range(4):
            nx = positon[1] + dx[i]
            ny = positon[0] + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] > visited[positon[0]][positon[1]] + board[ny][nx]:
                    visited[ny][nx] = now+board[ny][nx]
                    heapq.heappush(hq,(now+board[ny][nx],(ny,nx)))
    
    print("Problem "+str(problem) +": " + str(visited[N-1][N-1]))
    problem+=1 

