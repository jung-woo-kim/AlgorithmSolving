import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

parent = [i for i in range(N+1)]

def find(parent,x):
    if x != parent[x]:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
for _ in range(M):
    z, a, b = map(int, input().split())
    
    if z == 0 :
        union(parent, a, b)
    else :
        if find(parent, a) == find(parent, b):
            print('YES')
        else :
            print('NO')

    print(parent)