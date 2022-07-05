import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

result = 1e9

def dfs(depth,n):
    global result
    if n > K:
        return
    elif n == K:
        result = min(result,depth)
        return

    for i in range(0,2):
        if i == 0:
            dfs(depth+1,n*2)
        if i == 1:
            dfs(depth+1,int(str(n)+'1'))

dfs(0,N)

if result == 1e9:
    print('-1')
else:
    print(result+1) 