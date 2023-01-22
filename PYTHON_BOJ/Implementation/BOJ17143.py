import sys

R,C,M = map(int,sys.stdin.readline().rstrip().split())

shark = []
answer = 0

dx = [0,0,1,-1]
dy = [-1,1,0,0]

board = [[[] for _ in range(C)] for __ in range(R)]

for _ in range(M):
    s = list(map(int,sys.stdin.readline().rstrip().split()))
    board[s[0]-1][s[1]-1] = [s[2],s[3],s[4]]

R_cycle = [i for i in range(R)]
R_cycle += [i for i in range(R-2,0,-1)]
C_cycle = [i for i in range(C)]
C_cycle += [i for i in range(C-2,0,-1)]


for i in range(C):
    
    for r in range(R):
        if len(board[r][i]) != 0:
            answer += board[r][i][2]
            board[r][i] = []
            
            break
    
    new_board = [[[] for _ in range(C)] for __ in range(R)]
    for r in range(R):
        for c in range(C):
            if len(board[r][c]) != 0:
                s,d,z = board[r][c]
                if d == 1 or d == 2:
                    nr = R_cycle[(r+s *dy[d-1]) % (R*2 -2)]
                    nc = c

                    if (r+s *dy[d-1]) % (R*2 -2) >= (R*2 -2) //2:
                        if d == 1:
                            d = 2
                        else:
                            d = 1 

                else:
                    nc = C_cycle[(c+s *dx[d-1]) % (C*2 -2)]
                    nr = r

                    if (c+s *dx[d-1]) % (C*2 -2) >= (C*2 -2) //2:
                        if d == 3:
                            d = 4
                        else:
                            d = 3 
                
                if new_board[nr][nc]:
                    if new_board[nr][nc][2] < z:
                        new_board[nr][nc] = [s,d,z]
                else:
                    new_board[nr][nc] = [s,d,z]

    board = new_board

print(answer)

                