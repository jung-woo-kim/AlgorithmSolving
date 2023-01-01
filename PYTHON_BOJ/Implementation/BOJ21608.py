import sys

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def check1(like):
    passed = []
    now = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                liked = likedNum(r,c,like)
                if liked > now:
                    now = liked
                    passed = [[r,c]]
                elif liked == now:
                    passed.append((r,c))
    return passed

def check2(check1_passed):
    passed = []
    now = 0
    for r,c in check1_passed:
        empty = emptyNum(r,c)
        if empty > now:
            now = empty
            passed = [[r,c]]
        elif empty == now:
            passed.append([r,c])
    return passed

def emptyNum(r,c):
    num = 0

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0<= nr < N and 0 <= nc <N:
            if board[nr][nc] == 0:
                num += 1
    return num

def likedNum(r,c,like):
    num = 0

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0<= nr < N and 0 <= nc <N:
            if board[nr][nc] in like:
                num += 1
    return num

def getTotalSatisfied():
    student = sorted(liked)
    total = 0
    for r in range(N):
        for c in range(N):
            total += getSatisfied(r,c,[student[board[r][c]-1][1],student[board[r][c]-1][2],student[board[r][c]-1][3],student[board[r][c]-1][4]])
    return total
    
def getSatisfied(r,c,like):
    num = 0

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0<= nr < N and 0 <= nc <N:
            if board[nr][nc] in like:
                num += 1
    
    if num == 4:
        return 1000
    elif num == 3:
        return 100
    elif num == 2:
        return 10
    elif num == 1:
        return 1
    else:
        return 0

N = int(sys.stdin.readline().rstrip())

liked = []
board = [[0 for _ in range(N)] for __ in range(N)]

for _ in range(N**2):
    S,L1,L2,L3,L4 = map(int,sys.stdin.readline().rstrip().split())
    liked.append([S,L1,L2,L3,L4])

for s,l1,l2,l3,l4 in liked:
    check1_passed = check1([l1,l2,l3,l4])
    check2_passed = check2(check1_passed)
    check3 = sorted(check2_passed, key = lambda x : x[1])
    check3_passed = sorted(check3, key = lambda x : x[0])

    board[check3_passed[0][0]][check3_passed[0][1]] = s

print(getTotalSatisfied())