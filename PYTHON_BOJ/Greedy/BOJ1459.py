import sys

X,Y,W,S = map(int,sys.stdin.readline().rstrip().split())

if 2*W > S:
    print(min(X,Y)*S + abs(X-Y)*S)
else:
    print(min(X,Y)*2*W + abs(X-Y)*W)
