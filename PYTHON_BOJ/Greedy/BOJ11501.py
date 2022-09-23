import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    stock = list(map(int,sys.stdin.readline().rstrip().split()))
    n_max = 0
    answer = 0
    for i in range(N-1,-1,-1):
        if stock[i] >= n_max:
            n_max = stock[i]
        else:
            answer += n_max - stock[i]

    print(answer)