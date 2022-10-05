from copy import deepcopy
import sys

T = int(sys.stdin.readline().rstrip())

def reverse(n,board):
    if 0 <= n <= 2:
        for i in range(3):
            board[n][i] = -board[n][i]
    elif 3<= n <= 5:
        for i in range(3):
            board[i][n-3] = -board[i][n-3]
    elif n == 6:
        for i in range(3):
            board[i][i] = -board[i][i]
    else:
        board[2][0] = -board[2][0]
        board[1][1] = -board[1][1]
        board[0][2] = -board[0][2]

def checking(board):
    check = 0
    for y in range(3):
        check += sum(board[y])

    if check == 9 or check == -9:
        return True
    else:
        return False
combination = [[] for _ in range(8)]
def DFS(start,li,depth):
  
    combi = list(map(int,(li.split())))
    combination[len(combi)-1].append(combi)

    for i in range(start,8):
        tmp = ""
        tmp += li + str(i) + " "
        DFS(i+1,tmp,depth + 1)
DFS(0,"",0)


for _ in range(T):
    coin = []
    for __ in range(3):
        coin.append(sys.stdin.readline().rstrip().split())
    
    for y in range(3):
        for x in range(3):
            if coin[y][x] == "H":
                coin[y][x] = 1
            else:
                coin[y][x] = -1
    check = False
    if checking(coin):
        check = True
        print(0)
        
    for i in range(len(combination)):
        if check:
            break
        for li in combination[i]:
            copy = deepcopy(coin)
            for j in li:
                reverse(j,copy)
            if checking(copy):
                print(i+1)
                check = True
                break
    
    if not check:
        print(-1)
    
    