from copy import copy
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
li = list(map(int,sys.stdin.readline().rstrip().split()))

li.sort()

def DFS(depth,nums):
    if depth == M:
        print(*nums)
        return
    
    for i in range(0,N):
        tmp = copy(nums)
        tmp.append(li[i])
        DFS(depth+1,tmp)

DFS(0,[])