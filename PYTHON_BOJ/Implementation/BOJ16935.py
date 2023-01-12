import sys

N, M, R = map(int,sys.stdin.readline().rstrip().split())

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split()))) 

def calc_one():
    start = 0
    end = N-1

    while start < end:
        temp = board[start]
        board[start] = board[end]
        board[end] = temp

        start += 1
        end -= 1

def calc_two():
    start = 0
    end = M-1

    while start < end:
        for i in range(N):
            temp = board[i][start]
            board[i][start] = board[i][end]
            board[i][end] = temp
        start += 1
        end -= 1

def calc_three():
    global N
    global M
    global board
    new_board = []
    for x in range(M):
        temp = []
        for y in range(N-1,-1,-1):
            temp.append(board[y][x])
        new_board.append(temp)
    board = new_board

    N,M = M,N

def calc_four():
    global board
    global N
    global M
    new_board = []
    for x in range(M-1,-1,-1):
        temp = []
        for y in range(N):
            temp.append(board[y][x])
        new_board.append(temp)
    board = new_board
    N,M = M,N

def four_part():
    one = []
    two = []
    three = []
    four = []

    for y in range(N//2):
        one.append(board[y][:M//2])
        two.append(board[y][M//2:])
    for y in range(N//2,N):
        four.append(board[y][:M//2])
        three.append(board[y][M//2:])

    return one,two,three,four


def calc_five():
    global board
    one,two,three,four = four_part()
    first = four + three
    second = one + two

    for y in range(N):
        for x in range(M//2):
            first[y].append(second[y][x])
    
    board = first

def calc_six():
    global board
    one,two,three,four = four_part()
    first = two + one
    second = three +four

    for y in range(N):
        for x in range(M//2):
            first[y].append(second[y][x])
    
    board = first
nums = list(map(int,sys.stdin.readline().rstrip().split()))
for num in nums:

    if num == 1:
        calc_one()
    elif num == 2:
        calc_two()
    elif num == 3:
        calc_three()
    elif num == 4:
        calc_four()
    elif num == 5:
        calc_five()
    else:
        calc_six()

for y in range(len(board)):
    print(*board[y])
    