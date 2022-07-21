import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().rstrip().split())
    if M <= N:
        nx = x
        ny = x
        answer = x
    else:
        nx = y
        ny = y
        answer = y

    while True:
        if answer > N*M:
            print(-1)
            break

        if nx == x and ny == y:
            print(answer)
            break
        if M <= N:
            if ny == 0 and y == N:
                print(answer)
                break
    
            ny += M
            ny %= N
            answer += M
        else:
            if nx == 0 and x == M:
                print(answer)
                break
    
            nx += N
            nx %= M
            answer += N

        