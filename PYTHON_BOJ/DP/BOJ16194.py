import sys

N = int(sys.stdin.readline().rstrip())

cards = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [i*cards[0] for i in range(0,N+1)]


for i in range(2,N+1):
    for j in range(i,N+1):
        if dp[j] > dp[j-i] + cards[i-1]:
            dp[j] = dp[j-i] + cards[i-1]
    
    print(dp)