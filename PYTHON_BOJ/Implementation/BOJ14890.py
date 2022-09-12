import sys

N,L = map(int,sys.stdin.readline().rstrip().split())

board = []

for y in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

runway = [[0 for _ in range(N)] for __ in range(N)]

answer = 0

for y in range(N):
    for x in range(N-1):
        check = False

        if board[y][x] == board[y][x+1]:
            pass
        elif board[y][x] > board[y][x+1]:
            for l in range(1,L+1):
                if x + l >= N:
                    check = True
                    break

                if board[y][x]-board[y][x+l] == 1 and runway[y][x+l] == 0:
                    runway[y][x+l] = 1
                else:
                    check = True
                    break
        else:
            for l in range(1,L+1):
                if x+1-l < 0:
                    check = True
                    break

                if board[y][x+1]-board[y][x+1-l] == 1 and runway[y][x+1-l] == 0:
                    runway[y][x+1-l] = 1
                else:
                    check = True
                    break
            
        if check:
            break

        if x == N-2:
            answer+=1
            



runway = [[0 for _ in range(N)] for __ in range(N)]

for x in range(N):
    for y in range(N-1):
        check = False

        if board[y][x] == board[y+1][x]:
            pass
        elif board[y][x] > board[y+1][x]:

            for l in range(1,L+1):

                if y + l >= N:
                    check = True
                    break

                if board[y][x]-board[y+l][x] == 1 and runway[y+l][x] == 0:
                    runway[y+l][x] = 1
                else:
                    check = True
                    break
        else:
            for l in range(1,L+1):
                if y+1-l < 0:
                    check = True
                    break
                if board[y+1][x]-board[y+1-l][x] == 1 and runway[y+1-l][x] == 0:
                    runway[y+1-l][x] = 1
                else:
                    check = True
                    break
        if check:
            break

        if y == N-2:
            answer+=1
        

print(answer)