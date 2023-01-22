import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    li = list(map(int,sys.stdin.readline().rstrip().split()))

    S = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        S[i] = S[i-1] + li[i-1]
    
    DP = [[0 for _ in range(N+1)] for __ in range(N+1)]

    # 파일의 길이
    for i in range(2,N+1):
        # 시작점 순환
        for j in range(1,N+2-i):
            # 파일의 길이 내부에서도 선택 점들이 있다.
            # 1~4라면 12 24 13 34 처럼
            DP[j][j+i-1] = min(DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)) + S[j+i-1] -S[j-1]
    
    print(DP[1][N])