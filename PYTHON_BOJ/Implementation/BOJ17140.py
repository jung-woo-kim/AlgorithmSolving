import sys

r, c, k = map(int,sys.stdin.readline().rstrip().split())

board = []

now_r = 3
now_c = 3

for _ in range(3):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def R_calc():

    global now_c
    max_len = 0
    li = []

    for y in range(now_r):
        num_list = [[i,0] for i in range(101)]
        tmp = []
        for x in range(now_c):
            if board[y][x] != 0:
                num_list[board[y][x]][1] += 1
        for x in range(101):
            if num_list[x][1] != 0:
                tmp.append(num_list[x])
        tmp.sort()
        tmp.sort(key = lambda x : x[1])
        max_len = max(max_len,len(tmp) * 2)
        li.append(tmp)

    for y in range(now_r):
        board[y] = make_num_to_list(li[y], max_len)
    now_c = max_len

def C_calc():

    global board
    global now_r
    max_len = 0
    li = []

    for x in range(now_c):
        num_list = [[i,0] for i in range(101)]
        tmp = []
        for y in range(now_r):
            if board[y][x] != 0:
                num_list[board[y][x]][1] += 1
                tmp.append(board[y][x])
        
        tmp = list(set(tmp))
        new_tmp = []
        for t in tmp:
            new_tmp.append(num_list[t])
        tmp = new_tmp

        tmp.sort()
        tmp.sort(key = lambda x : x[1])
        max_len = max(max_len,len(tmp) * 2)
        li.append(tmp)
    tmp = []
    for x in range(now_c):
        tmp.append(make_num_to_list(li[x], max_len)) 
    board = list(zip(*tmp))
    now_r = max_len
    

def make_num_to_list(li,max_len):
    new = []
    for num,num_appear in li:
        new.append(num)
        new.append(num_appear)
    new += [0] * (max_len - len(li)*2)
    if len(new) > 100:
        new = new[:100]

    return new

for i in range(101):
    try:
        if board[r - 1][c - 1] == k:
            print(i)
            break
    except: pass
    if now_r >= now_c:
        R_calc()
    else:
        C_calc()
else:
    print(-1)
