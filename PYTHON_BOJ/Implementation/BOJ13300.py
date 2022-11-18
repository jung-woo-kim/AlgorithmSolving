import sys

N,K = map(int,sys.stdin.readline().split())
li =[0 for _ in range(12)]

for _ in range(N):
    S,G = map(int,sys.stdin.readline().split())
    if S == 0:
        li[G-1] += 1
    if S == 1:
        li[6 + G-1] += 1

answer = 0

for i in range(12):
    answer += li[i] // K
    if li[i] % K != 0:
        answer += 1

print(answer)