import sys

N,M,y,x,K = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

move = list(map(int,sys.stdin.readline().rstrip().split()))

#위 아래 좌 우 앞 뒤 
dice = [0,0,0,0,0,0]

def move_dice_buk():
    tmp = dice.copy()
    dice[0] = tmp[5]
    dice[1] = tmp[4]
    dice[2] = tmp[2]
    dice[3] = tmp[3]
    dice[4] = tmp[0]
    dice[5] = tmp[1]

def move_dice_nam():
    tmp = dice.copy()
    dice[0] = tmp[4]
    dice[1] = tmp[5]
    dice[2] = tmp[2]
    dice[3] = tmp[3]
    dice[4] = tmp[1]
    dice[5] = tmp[0]

def move_dice_dong():
    tmp = dice.copy()
    dice[0] = tmp[3]
    dice[1] = tmp[2]
    dice[2] = tmp[0]
    dice[3] = tmp[1]
    dice[4] = tmp[4]
    dice[5] = tmp[5]

def move_dice_seo():
    tmp = dice.copy()
    dice[0] = tmp[2]
    dice[1] = tmp[3]
    dice[2] = tmp[1]
    dice[3] = tmp[0]
    dice[4] = tmp[4]
    dice[5] = tmp[5]

for i in range(K):
    if move[i] == 1:
        if x + 1 < M:
            move_dice_dong()
            x += 1
            if board[y][x] == 0:
                board[y][x] = dice[1]
            else:
                dice[1] = board[y][x]
                board[y][x] = 0
            print(dice[0])

    if move[i] == 2:
        if x - 1 >= 0:
            move_dice_seo()
            x -= 1
            if board[y][x] == 0:
                board[y][x] = dice[1]
            else:
                dice[1] = board[y][x]
                board[y][x] = 0
            print(dice[0])

    if move[i] == 3:
        if y - 1 >= 0:
            move_dice_buk()
            y -= 1
            if board[y][x] == 0:
                board[y][x] = dice[1]
            else:
                dice[1] = board[y][x]
                board[y][x] = 0
            print(dice[0])

    if move[i] == 4:
        if y + 1 < N:
            move_dice_nam()
            y += 1
            if board[y][x] == 0:
                board[y][x] = dice[1]
            else:
                dice[1] = board[y][x]
                board[y][x] = 0
            print(dice[0])

