import sys
import copy

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

visited = [False for _ in range(N)]
answer = 0

def DFS(l,depth):
    global answer
    if depth == N-2:
        tmp = copy.copy(li)
        value = 0
        for idx in l:
            value += tmp[idx-1] * tmp[idx+1]
            
            tmp = tmp[:idx] + tmp[idx+1:]
        answer = max(answer,value) 
        return

    for i in range(1,N-1-depth):
        tmp = copy.copy(l)
        tmp.append(i)
        DFS(tmp,depth+1)

DFS([],0)
print(answer)