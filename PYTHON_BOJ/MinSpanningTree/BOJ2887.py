import sys
            
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

N = int(sys.stdin.readline().rstrip())

planets = []

for i in range(N):
    x,y,z = map(int,sys.stdin.readline().rstrip().split())
    planets.append((i,x,y,z))

edges = []

parent = [i for i in range(N)]

sort = sorted(planets, key = lambda x: x[1])

for i in range(1,N):
    m = min(abs(sort[i][3] - sort[i-1][3]),abs(sort[i][1] - sort[i-1][1]),abs(sort[i][2] - sort[i-1][2]))
    edges.append((m,sort[i][0],sort[i-1][0]))

sort = sorted(planets, key = lambda x: x[2])

for i in range(1,N):
    m = min(abs(sort[i][3] - sort[i-1][3]),abs(sort[i][1] - sort[i-1][1]),abs(sort[i][2] - sort[i-1][2]))
    edges.append((m,sort[i][0],sort[i-1][0]))

sort = sorted(planets, key = lambda x: x[3])

for i in range(1,N):
    m = min(abs(sort[i][3] - sort[i-1][3]),abs(sort[i][1] - sort[i-1][1]),abs(sort[i][2] - sort[i-1][2]))
    edges.append((m,sort[i][0],sort[i-1][0]))

edges.sort()

answer = 0

for m,a,b in edges:
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            parent[b] = a
        else:
            parent[a] = b
        answer += m

print(answer)

