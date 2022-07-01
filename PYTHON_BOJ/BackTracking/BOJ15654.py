import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

li = list(map(int,sys.stdin.readline().rstrip().split()))
li.sort()
visited = [False for _ in range(N)]

def dfs(depth,l):
    if depth == M:
        print(l)
        return
    
    for i in range(0,N):
        if not visited[i]:
            visited[i] = True
            temp = ""
            temp = l + str(li[i])+" "
            dfs(depth+1,temp)
            visited[i] = False

dfs(0,"")