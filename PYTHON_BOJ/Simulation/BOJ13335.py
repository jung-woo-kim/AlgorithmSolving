from collections import deque
import sys

n,w,L = map(int,sys.stdin.readline().rstrip().split())

truck = list(map(int,sys.stdin.readline().rstrip().split()))

idx = 0
now_weight = 0
bridge = deque()

for t in range(0,n*w+1):

    if idx == n:
        print(t+w)
        exit()

    for i in range(len(bridge)):
        bridge[i][1] += 1
    

    if bridge and bridge[0][1] == w:
        now_weight -= bridge[0][0]
        bridge.popleft()

    if truck[idx] <= L - now_weight:
        now_weight += truck[idx]
        bridge.append([truck[idx],0])
        idx+=1
    
    

          