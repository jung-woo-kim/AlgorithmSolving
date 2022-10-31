from copy import copy
import sys

N,M,K = map(int,sys.stdin.readline().split())

board = []
answer = 0

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

def DFS(depth,start,li):
    global answer

    if depth == K:
        print(li)
        position = []
        for item in li:
            r = item // M
            c = item % M
            position.append((r,c))
        if distanceCheck(position):
            
            sum = 0
            for r,c in position:
                sum += board[r][c]
            answer = max(answer,sum)

    for i in range(start,N*M):
        tmp = copy(li)
        tmp.append(i)
        DFS(depth+1,i+1,tmp)

def distanceCheck(position):
    for r1,c1 in position:
        for r2,c2 in position:
            if abs(r1-r2) + abs(c1-c2) == 1:
                return False
    
    return True

DFS(0,0,[])
print(answer)