from copy import copy
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
li = list(map(int,sys.stdin.readline().rstrip().split()))

li.sort()

def DFS(depth,start,nums):
    if depth == M:
        print(*nums)
    
    for i in range(start,N):
        tmp = copy(nums)
        tmp.append(li[i])
        DFS(depth+1,i+1,tmp)

DFS(0,0,[])