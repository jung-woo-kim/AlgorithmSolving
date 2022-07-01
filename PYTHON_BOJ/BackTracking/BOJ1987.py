import sys

R,C = map(int,sys.stdin.readline().rstrip().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
alphabet =[False for i in range(26)]
alphabet[ord(board[0][0])-65] = True
result = 0

def dfs(x,y,al,depth):
    global result

    result = max(result,depth)
   
    for i in range(0,4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and ny >=0 and nx < C and ny < R:
            if not al[ord(board[ny][nx])-65]:
                al[ord(board[ny][nx])-65] = True     
                
                dfs(nx,ny,al,depth+1)
                al[ord(board[ny][nx])-65] = False        

            

dfs(0,0,alphabet,1)

print(result)