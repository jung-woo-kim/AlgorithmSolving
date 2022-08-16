import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

god = []
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if parent[a] > parent[b]:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

for _ in range(N):
    x,y = map(int,sys.stdin.readline().rstrip().split())

    god.append((x,y))

for _ in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    union(a,b)

edge = []

for i in range(N):
    for j in range(i+1,N):
        c = ((god[i][0] - god[j][0])**2 + (god[i][1] - god[j][1])**2)**0.5
        edge.append([c,i+1,j+1])

edge.sort()
answer = 0

for c,a,b in edge:
    a_parent = find(a)
    b_parent = find(b)

    if a_parent != b_parent:
        if a_parent<b_parent:
            parent[b_parent] = a_parent
        else:
            parent[a_parent] = b_parent
        answer += c

print(format(answer,".2f"))


