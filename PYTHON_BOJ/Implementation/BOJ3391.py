import sys

h,w,c = map(int,sys.stdin.readline().rstrip().split())


color = list(map(int,sys.stdin.readline().rstrip().split()))

board =[[0 for __ in range(w)] for _ in range(h)]

tmp = 0

for i in range(c):
    num = color[i]
    if tmp == 0:
        tmp = 1
        for y in range(h):
            for x in range(w):
                if board[y][x] == 0 and num >0:
                    num -= 1
                    board[y][x] = i+1
    else:
        tmp = 0
        for y in range(h):
            for x in range(w-1,-1,-1):
                if board[y][x] == 0 and num >0:
                    num -= 1
                    board[y][x] = i+1

for y in range(h):
    st = ""
    for x in range(w):
        st += str(board[y][x])
    print(st)
