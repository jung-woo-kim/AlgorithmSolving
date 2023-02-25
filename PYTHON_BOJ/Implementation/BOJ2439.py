import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N-1,-1,-1):
    tmp = " "*i + "*"*((i-N)*-1)
    print(tmp)