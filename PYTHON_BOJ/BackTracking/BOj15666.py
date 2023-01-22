import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

li = list(set(map(int,sys.stdin.readline().rstrip().split())))
li.sort()
arr = []

def DFS(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(len(li)):
        if depth == 0 or arr[-1] <= li[i] :
            arr.append(li[i])
            DFS(depth+1)
            arr.pop()

DFS(0)