import sys
from copy import deepcopy

N = int(sys.stdin.readline().rstrip())

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def move_right(board):

    new_board = []

    for y in range(N):
        temp = []
        flag = True
        for x in range(N-1,-1,-1):
            if board[y][x] == 0:
                continue
            if not temp:
                temp.append(board[y][x])
            else:
                if flag and temp[-1] == board[y][x]:
                    temp.append(temp.pop()*2)
                    flag = False
                else:
                    temp.append(board[y][x])
                    flag = True
        for _ in range(N-len(temp)):
            temp.append(0)
        new_board.append(temp[::-1])
    
    return new_board

def move_left(board):

    new_board = []

    for y in range(N):
        temp = []
        flag = True
        for x in range(0,N):
            if board[y][x] == 0:
                continue
            if not temp:
                temp.append(board[y][x])
            else:
                if flag and temp[-1] == board[y][x]:
                    temp.append(temp.pop()*2)
                    flag = False
                else:
                    temp.append(board[y][x])
                    flag = True
        for _ in range(N-len(temp)):
            temp.append(0)
        new_board.append(temp)
    
    return new_board

def move_top(board):

    new_board = [[0 for _ in range(N)] for __ in range(N)]

    for x in range(N):
        temp = []
        flag = True
        for y in range(N):
            if board[y][x] == 0:
                continue
            if not temp:
                temp.append(board[y][x])
            else:
                if flag and temp[-1] == board[y][x]:
                    temp.append(temp.pop()*2)
                    flag = False
                else:
                    temp.append(board[y][x])
                    flag = True
    
        for _ in range(N-len(temp)):
            temp.append(0)
        
        for y in range(N):
            new_board[y][x] = temp[y]

    return new_board
    
def move_down(board):

    new_board = [[0 for _ in range(N)] for __ in range(N)]

    for x in range(N):
        temp = []
        flag = True
        for y in range(N-1,-1,-1):
            if board[y][x] == 0:
                continue
            if not temp:
                temp.append(board[y][x])
            else:
                if flag and temp[-1] == board[y][x]:
                    temp.append(temp.pop()*2)
                    flag = False
                else:
                    temp.append(board[y][x])
                    flag = True
                    
        for _ in range(N-len(temp)):
            temp.append(0)
        temp.reverse()
        for y in range(N):
            new_board[y][x] = temp[y]

    return new_board

arr = []
answer = 0
def DFS(depth):
    global answer
    if depth == 5:
        temp_board = deepcopy(board)
        for direction in arr:
            if direction == 0:
                temp_board = move_right(temp_board)
            elif direction == 1:
                temp_board = move_down(temp_board)
            elif direction == 2:
                temp_board = move_left(temp_board)
            else:
                temp_board = move_top(temp_board)
        
        for y in range(N):
            for x in range(N):
                answer = max(temp_board[y][x],answer)

        return

    for i in range(4):
        arr.append(i)
        DFS(depth+1)
        arr.pop()
DFS(0)
print(answer)
