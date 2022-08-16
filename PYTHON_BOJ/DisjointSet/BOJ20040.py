import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

parent = [i for i in range(N)]

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(M):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    if find(parent,a) == find(parent,b):
        print(i+1)
        exit()
    union(parent,a,b)
    
print(0)