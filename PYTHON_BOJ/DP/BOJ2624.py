from random import randrange
import sys

T = int(sys.stdin.readline().rstrip())

k = int(sys.stdin.readline().rstrip())

coin = []

for _ in range(k):
    p,n = map(int,sys.stdin.readline().rstrip().split())
    coin.append((p,n))

dp = [0 for _ in range(T+1)]
dp[0] = 1

for c,num in coin:
    for i in range(T,0,-1):
        for j in range(1,num+1):
            if i-c*j>=0:
                dp[i] += dp[i-c*j]
                
                

print(dp)                    

