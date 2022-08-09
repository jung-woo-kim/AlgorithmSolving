import sys

M,N = map(int,sys.stdin.readline().rstrip().split())

if M<=N:
    print(2*(M-1))
else:
    print(2*(N-1)+1)