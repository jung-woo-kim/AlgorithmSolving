from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(N+1)]
tree_info = [["",0] for _ in range(N+1)]
leaf = [0 for _ in range(N+1)]

for i in range(2,N+1):   
    t,a,p = sys.stdin.readline().rstrip().split()
    tree_info[i][0] = t
    tree_info[i][1] = int(a)
    tree[i].append(int(p))
    leaf[int(p)] = 1

answer = 0
q = deque()

for i in range(2,N+1):
    if leaf[i] == 0:
        if tree_info[i][0] == "S":
            q.append((i,tree_info[i][1]))
        else:
            q.append((i,0))

while q:
    n,sheep = q.popleft()
    if n == 1:
        answer += sheep
        
    for node in tree[n]:
        if tree_info[node][0] == 'S':
            q.append((node,sheep+tree_info[node][1]))
            #양이 이미 갔으면 해당 구역의 양의 개수를 0으로
            tree_info[node][1] = 0
        else:
            #늑대가 양이 섬에 도착할때마다 먹는가? -> 먹는다
            if sheep > tree_info[node][1]:
                q.append((node,sheep - tree_info[node][1]))
                tree_info[node][1] = 0
            else:
                q.append((node,0))
                tree_info[node][1] -= sheep

print(answer)