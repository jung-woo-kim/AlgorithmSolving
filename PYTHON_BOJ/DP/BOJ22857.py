import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

S = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [[0,0] for _ in range(N)]

if S[0] % 2 == 0:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1,N):
    if S[i] % 2 == 0:
        dp[i][0] += dp[i-1][0]+1
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][1] += dp[i-1][1]+1
        dp[i][0] = dp[i-1][0]


lp = -1
rp = 0
answer = 0

while lp < N and rp < N and lp < rp:
    #홀수의 개수
    odd = 0

    if lp == -1:
        odd = dp[rp][1]
    else:
        odd = dp[rp][1] - dp[lp][1]

    if odd > K:
        lp+=1
    else:
        if lp == -1:
            answer = max(rp+1-odd,answer) 
        else:
            answer = max(rp-lp-odd,answer)
            
        rp+=1

print(answer)