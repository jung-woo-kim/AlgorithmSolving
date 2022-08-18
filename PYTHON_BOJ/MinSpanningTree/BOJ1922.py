import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

parent = [i for i in range(N+1)]

edge = []

for _ in range(M):
    A,B,C =  map(int,sys.stdin.readline().rstrip().split())
    edge.append((C,A,B))

edge.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

answer = 0
for w,a,b in edge:

    a_parent = find(a)
    b_parent = find(b)

    if a_parent != b_parent:
        if a_parent < b_parent:
            parent[b_parent] = a_parent
        else:
            parent[a_parent] = b_parent
        answer += w
 
        
print(answer)
    