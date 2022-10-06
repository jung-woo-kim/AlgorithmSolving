import sys

R,C,N = map(int,sys.stdin.readline().rstrip().split())
board = []

for _ in range(R):
    board.append(sys.stdin.readline().rstrip())

if N == 0:
    for y in range(R):
        str = ""
        for x in range(C):
            str += board[y][x]
        print(str)
    exit()

N -= 1

bomb = []
for y in range(R):
    for x in range(C):
        if board[y][x] == "O":
            bomb.append((y,x))

temp = [["O" for _ in range(C)]for __ in range(R)]

dx = [0,1,0,-1,0]
dy = [0,0,1,0,-1]

for y,x in bomb:
    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C: 
            temp[ny][nx] = "."
if N % 4 == 1 or N % 4 == 3:
    for _ in range(R):
        print("0"*C)
elif N % 4 == 2:
    for y in range(R):
        str = ""
        for x in range(C):
            str += temp[y][x]
        print(str)
elif N % 4 == 0:
    for y in range(R):
        str = ""
        for x in range(C):
            str += board[y][x]
        print(str)