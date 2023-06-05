from collections import deque

def solution(board):
    answer = 0
    o_check = False
    x_check = False
    o_num = 0
    x_num = 0
    for i in range(3):
        if board[i] == "OOO":
            o_check = True
        if board[i] == "XXX":
            x_check = True
    
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            o_check = True 
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            x_check = True 
        for j in range(3):
            if board[i][j] == "O":
                o_num += 1
            if board[i][j] == "X":
                x_num += 1

    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        o_check = True

    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        x_check = True
    
    if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        o_check = True
    
    if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        x_check = True
    

    if not (o_num == x_num +1 or o_num == x_num):
        return answer
    
    if x_check and o_check:
        return answer
    if o_check:
        if o_num == x_num:
            return answer
    if x_check:
        if o_num>x_num:
            return answer

    return 1