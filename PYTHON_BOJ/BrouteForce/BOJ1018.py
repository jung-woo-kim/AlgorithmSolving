import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

answer = 1e9
board = []
def find(standard):
    temp = 0
    for y in range(0,8):
        for x in range(0,8):
                
            if standard == board[y+off_y][x+off_x]:
                temp += 1
                if standard == "W":
                    standard = "B"
                else:
                    standard = "W"
            else:
                standard = board[y+off_y][x+off_x]

            if x == 7:
                if standard == "W":
                    standard = "B"
                else:
                    standard = "W"
    return temp
for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

for off_x in range(0,M-7):
    for off_y in range(0,N-7):
        standard = ""
        
        for i in range(2):
            t = 0
            if i == 0:
                if board[off_y][off_x] == "W":
                    standard = "B"
                else:
                    standard = "W"
                
            else:
                standard = board[off_y][off_x]
                
            t = find(standard)
            answer = min(answer,t)
        
print(answer)