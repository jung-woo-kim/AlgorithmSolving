import sys

N,M,R = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def rotate_north(depth):
    for x in range(depth,M-depth-1):
        temp = board[depth][x]
        board[depth][x] = board[depth][x+1]
        board[depth][x+1] =temp
    
    return temp

def rotate_east(depth,start):
    temp = board[depth+1][depth]

    for y in range(N-depth-1,depth+1,-1):
        temp = board[y][depth]
        board[y][depth] = board[y-1][depth]
        board[y-1][depth] = temp

    board[depth+1][depth] = start
    return temp

def rotate_south(depth,start):
    temp = board[N-depth-1][depth+1]

    for x in range(M-depth-1,depth+1,-1):
        temp = board[N-depth-1][x]
        board[N-depth-1][x] = board[N-depth-1][x-1]
        board[N-depth-1][x-1] = temp
    
    board[N-depth-1][depth+1] = start
    return temp

def rotate_west(depth,start):

    temp = board[depth+1][M-1-depth]

    for y in range(depth+1,N-depth-2):
        temp = board[y][M-1-depth]
        board[y][M-1-depth] = board[y+1][M-1-depth]
        board[y+1][M-1-depth] = temp
    
    board[depth][M-1-depth] = temp
    board[N-depth-2][M-depth-1] = start

cycle = (N-1) * 2 + (M-1) * 2

for depth in range(min(N,M)//2):
    for _ in range(R%cycle):
        temp = rotate_north(depth)
        temp = rotate_east(depth,temp)
        temp = rotate_south(depth,temp)
        rotate_west(depth,temp)
    cycle -= 8

for y in range(N):
    print(*board[y])