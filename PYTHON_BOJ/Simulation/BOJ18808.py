from copy import copy, deepcopy
import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split())

sticker = []

for _ in range(K):
    R,C = map(int,sys.stdin.readline().rstrip().split())
    s = []
    for _ in range(R):
        s.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    sticker.append(s)

board = [[0 for _ in range(M)]for __ in range(N)]

def rotate(sticker):
    s = deepcopy(sticker)
    return [[row[i] for row in s[::-1]] for i in range(len(s[0]))]


for i in range(K):
    board_check = True
    for j in range(4):
        if board_check:
            for y in range(N - len(sticker[i])+1):
                for x in range(M - len(sticker[i][0])+1):
                    #시작점
                    check = True
                    for s_y in range(len(sticker[i])):
                        for s_x in range(len(sticker[i][0])):
                            if board[s_y+y][s_x+x] == 1 and sticker[i][s_y][s_x] == 1:
                                check = False
                                break
                        if not check:
                            break

                    if check:
                        board_check = False
                        for s_y in range(len(sticker[i])):
                            for s_x in range(len(sticker[i][0])):
                                if sticker[i][s_y][s_x] == 1:
                                    board[s_y+y][s_x+x] = 1
                        break
                if not board_check:
                    break
            if board_check:    
                sticker[i] = rotate(sticker[i])
        else:
            break
answer = 0     
for y in range(N):
    answer += sum(board[y])

print(answer)