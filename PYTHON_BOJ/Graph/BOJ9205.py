from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())
def BFS(s_x,s_y,store):
    q = deque()
    q.append((s_x,s_y))
    visited = [False for _ in range(len(store))]

    while q:
        x,y = q.popleft()

        if x == store[-1][0] and y == store[-1][1]:
            return "happy" 

        for i in range(len(store)):
            if not visited[i]:
                if abs(store[i][0]-x) + abs(store[i][1] - y) <= 1000:
                    q.append((store[i][0],store[i][1]))
                    visited[i] = True
        
    return "sad"
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    home = list(map(int,sys.stdin.readline().rstrip().split()))
    store = []
    for __ in range(n):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        store.append((x,y))
    
    goal = list(map(int,sys.stdin.readline().rstrip().split()))
    store.append(goal)
    print(BFS(home[0],home[1],store))

