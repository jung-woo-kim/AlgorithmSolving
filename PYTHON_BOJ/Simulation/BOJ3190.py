from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

board = [[0 for _ in range(0,N)] for _ in range(0,N)]

snake = deque()

board[0][0] = 2
snake.append([0,0])
head = [0,0]

for _ in range(0,K):
    y,x = map(int,sys.stdin.readline().rstrip().split())
    board[y-1][x-1] = 1 #사과 1

L = int(sys.stdin.readline().rstrip())

direct = deque()
nx = [1,0,-1,0]
ny = [0,1,0,-1]
now_direct_idx=0

for _ in range(0,L):
    temp = sys.stdin.readline().rstrip().split()
    direct.append((int(temp[0]),temp[1]))

time = 1

while True:
    if time == direct[0][0]:
        if direct[0][1] == 'D':
            now_direct_idx += 1
            if now_direct_idx > 3:
                now_direct_idx -= 4
        else:
            now_direct_idx -= 1
            if now_direct_idx < 0:
                now_direct_idx += 4
            
        direct.popleft()
    
    head[0] += ny[now_direct_idx]
    head[1] += nx[now_direct_idx]
    snake.append(head)

    print(head)
    if head[0] >= N or head[0] < 0 or head[1] >= N or head[1] < 0:
        break
    if board[head[0]][head[1]] == 2:
        break

    if board[head[0]][head[1]] == 1:
        board[head[0]][head[1]] = 2
        y,x = snake.popleft()
        board[y][x] = 0
        print('check')
    else:
        board[head[0]][head[1]] = 2
    
    time += 1

print(time)