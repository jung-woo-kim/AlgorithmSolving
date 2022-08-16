import sys

V, E = map(int,sys.stdin.readline().rstrip().split())

parent = [i for i in range(V+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

edges = []
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    edges.append((c,a,b))

edges.sort()
answer = 0
for c,a,b in edges:
    a_parent = find(a)
    b_parent = find(b)

    if a_parent != b_parent:
        if a_parent > b_parent:
            parent[a_parent] = b_parent
        else:
            parent[b_parent] = a_parent
        answer += c

print(answer)