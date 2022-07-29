from collections import deque
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

b_location = (-1,-1)
r_location = (-1,-1)
g_location = (-1,-1)



for y in range(N):
    for x in range(M):
        if board[y][x] == "B":
            b_location = (y,x)
        elif board[y][x] == "R":
            r_location = (y,x)
        elif board[y][x] == "O":
            g_location = (y,x)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def left(y,x,dy,dx):
    
    while True:
        
        x = x-1

        if (dy == y and x == dx) or x < 1 or board[y][x] == "#":
            x = x + 1 
            break

        if M-2 > x > 0 and board[y][x] == "O":
            return (-1,-1)
    
    return y,x

def right(y,x,dy,dx):
    
    while True:
        
        x = x+1
        if (dy == y and x == dx) or x > M-1  or board[y][x] == "#":
            x = x-1
            break
        if M-1 > x > 0 and board[y][x] == "O":
            return (-1,-1)
    
    return y,x

def top(y,x,dy,dx):
    
    while True:
        
        y = y - 1
        if (dy == y and x == dx) or y < 1  or board[y][x] == "#":
            y = y + 1
            break
        if N-1 > y > 0 and board[y][x] == "O":
            return (-1,-1)
    
    return y,x

def bottom(y,x,dy,dx):
    
    while True:
        
        y = y + 1
        if (dy == y and x == dx) or y > N-1 or board[y][x] == "#":
            y = y-1
            break

        if N-1 > y > 0 and board[y][x] == "O":
            return (-1,-1)
    
    return y,x

def bfs():
    queue = deque()
  
    queue.append((b_location,r_location))
    queue.append(-1)
    answer = 1
    visited = [[[[False for _ in range(M)]for __ in range(N)]for _ in range(M)]for __ in range(N)]
    visited[b_location[0]][b_location[1]][r_location[0]][r_location[1]] = True

   

    while queue:
        temp = queue.popleft()
        if answer > 10:
            print(-1)
            exit()

        if temp == -1:
            if queue:
                queue.append(-1)
                answer += 1
            else:
                return
        else:
            if answer > 10:
                print(-1)
                return
            b_y = temp[0][0]
            b_x = temp[0][1]
            r_y = temp[1][0]
            r_x = temp[1][1]
         
            for i in range(4):
                #왼쪽 -> y가 같으면 x가 작은 애부터 옮겨야함
                if i == 0:
                    if r_y == b_y:
                        if b_x < r_x:

                            b_check = False
                            r_check = False

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = left(b_y,b_x,r_x,r_y)
                            if b_y_1 != -1 and b_x_1 != -1:
                                pass
                            else:
                                b_check = True

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = left(r_y,r_x,b_y_1,b_x_1)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))

                        else:
                            b_check = False
                            r_check = False

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = left(r_y,r_x,b_y,b_x)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = left(b_y,b_x,r_y_1,r_x_1)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))
                    else:
                        b_check = False
                        r_check = False

                        board[r_y][r_x] = "."
                        r_y_1,r_x_1 = left(r_y,r_x,b_y,b_x)
                        if r_y_1 != -1 and r_x_1 != -1:
                            board[r_y_1][r_x_1] = "R"
                        else:
                            r_check = True

                        board[b_y][b_x] = "."
                        b_y_1,b_x_1 = left(b_y,b_x,r_y_1,r_x_1)
                        if b_y_1 != -1 and b_x_1 != -1:
                            board[b_y_1][b_x_1] = "B"
                        else:
                            b_check = True
                            
                        # r만 들어왔을때
                        if not b_check and r_check:
                            print(answer)
                            exit()
                            #둘다 안들어왔을 때
                        elif not b_check and not r_check:
                            if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))

                #아래로 y좌표가 더 큰애가 먼저 실행되어야함
                elif i == 1:
                    if r_x == b_x:
                        if b_y > r_y:

                            b_check = False
                            r_check = False

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = bottom(b_y,b_x,r_y,r_x)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = bottom(r_y,r_x,b_y_1,b_x_1)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))

                        else:
                            b_check = False
                            r_check = False

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = bottom(r_y,r_x,b_y,b_x)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = bottom(b_y,b_x,r_y_1,r_x_1)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True

                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))
                    else:
                        b_check = False
                        r_check = False

                        board[r_y][r_x] = "."
                        r_y_1,r_x_1 = bottom(r_y,r_x,b_y,b_x)
                        if r_y_1 != -1 and r_x_1 != -1:
                            board[r_y_1][r_x_1] = "R"
                        else:
                            r_check = True

                        board[b_y][b_x] = "."
                        b_y_1,b_x_1 =  bottom(b_y,b_x,r_y_1,r_x_1)
                        if b_y_1 != -1 and b_x_1 != -1:
                            board[b_y_1][b_x_1] = "B"
                        else:
                            b_check = True

                            
                            # r만 들어왔을때
                        if not b_check and r_check:
                            print(answer)
                            exit()
                            #둘다 안들어왔을 때
                        elif not b_check and not r_check:
                            if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))
                
                #오른쪽
                elif i == 2:
                    if r_y == b_y:
                        if b_x > r_x:

                            b_check = False
                            r_check = False

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = right(b_y,b_x,r_y,r_x)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = right(r_y,r_x,b_y_1,b_x_1)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))

                        else:
                            b_check = False
                            r_check = False

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = right(r_y,r_x,b_y,b_x)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = right(b_y,b_x,r_y_1,r_x_1)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True

                            
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))
                    else:
                        b_check = False
                        r_check = False

                        board[b_y][b_x] = "."
                        b_y_1,b_x_1 = right(b_y,b_x,r_y,r_x)
                        if b_y_1 != -1 and b_x_1 != -1:
                            board[b_y_1][b_x_1] = "B"
                        else:
                            b_check = True

                        board[r_y][r_x] = "."
                        r_y_1,r_x_1 = right(r_y,r_x,b_y_1,b_x_1)
                        if r_y_1 != -1 and r_x_1 != -1:
                            board[r_y_1][r_x_1] = "R"
                        else:
                            r_check = True
                            
                        # r만 들어왔을때
                        if not b_check and r_check:
                            print(answer)
                            exit()
                        #둘다 안들어왔을 때
                        elif not b_check and not r_check:
                            if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))
                
                #위로
                elif i == 3:
                    if r_x == b_x:
                        if b_y < r_y:

                            b_check = False
                            r_check = False

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = top(b_y,b_x,r_y,r_x)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = top(r_y,r_x,b_y_1,b_x_1)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))

                        else:
                            b_check = False
                            r_check = False

                            board[r_y][r_x] = "."
                            r_y_1,r_x_1 = top(r_y,r_x,b_y,b_x)
                            if r_y_1 != -1 and r_x_1 != -1:
                                board[r_y_1][r_x_1] = "R"
                            else:
                                r_check = True

                            board[b_y][b_x] = "."
                            b_y_1,b_x_1 = top(b_y,b_x,r_y_1,r_x_1)
                            if b_y_1 != -1 and b_x_1 != -1:
                                board[b_y_1][b_x_1] = "B"
                            else:
                                b_check = True

                            
                            
                            # r만 들어왔을때
                            if not b_check and r_check:
                                print(answer)
                                exit()
                            #둘다 안들어왔을 때
                            elif not b_check and not r_check:
                                if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                    visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                    queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))
                    else:
                        b_check = False
                        r_check = False

                        board[r_y][r_x] = "."
                        r_y_1,r_x_1 = top(r_y,r_x,b_y,b_x)
                        if r_y_1 != -1 and r_x_1 != -1:
                            board[r_y_1][r_x_1] = "R"
                        else:
                            r_check = True

                        board[b_y][b_x] = "."
                        b_y_1,b_x_1 = top(b_y,b_x,r_y_1,r_x_1)
                        if b_y_1 != -1 and b_x_1 != -1:
                            board[b_y_1][b_x_1] = "B"
                        else:
                            b_check = True

                            
                            
                        # r만 들어왔을때
                        if not b_check and r_check:
                            print(answer)
                            exit()
                        #둘다 안들어왔을 때
                        elif not b_check and not r_check:
                            if not visited[b_y_1][b_x_1][r_y_1][r_x_1]:
                                visited[b_y_1][b_x_1][r_y_1][r_x_1] = True
                                queue.append(((b_y_1,b_x_1),(r_y_1,r_x_1)))

bfs()
print(-1)