from cmath import sqrt
import sys

n = int(sys.stdin.readline().rstrip())

star = []

for _ in range(n):
    x,y = map(float,sys.stdin.readline().rstrip().split())
    star.append([x,y])

edge = []

for i in range(len(star)):
    for j in range(i+1,len(star)):
        c = ((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5
        edge.append([c,i,j])

parent = [i for i in range(n)]    
edge.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

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

print(answer)
