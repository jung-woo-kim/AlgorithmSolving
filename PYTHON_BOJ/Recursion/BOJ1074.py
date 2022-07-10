import sys

N,r,c = map(int,sys.stdin.readline().rstrip().split())

dx = [0,1,0,1]
dy = [0,0,1,1]

answer = -1

width = 2**(N)

def recur(base_x,base_y):
    global answer

    for i in range(4):
        nx = base_x+dx[i]
        ny = base_y+dy[i]
        print("x : "+str(nx) + " y : "+str(ny))
        answer += 1
        if nx == c and ny == r:
           print(answer)
           return
    if base_x == width-2:
        recur((base_x+2)%width,(base_y+2)%width)
    else:
        recur((base_x+2)%width,base_y)

recur(0,0)