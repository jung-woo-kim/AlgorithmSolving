import sys


#도시의 수
N = int(sys.stdin.readline().rstrip())

#여행 계획의 수
M = int(sys.stdin.readline().rstrip())

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


for i in range(1,N+1):
    li = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if li[j] == 1:
            union(parent,i,j+1)

travel = list(map(int,sys.stdin.readline().rstrip().split()))

check = True

for i in range(0,M-1):
    if find(parent,travel[i]) != find(parent,travel[i+1]):
        check = False

if check:
    print("YES")
else:
    print("NO")