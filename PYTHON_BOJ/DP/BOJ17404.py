from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

house = []
min_house = []


for _ in range(N):
    R,G,B = map(int,sys.stdin.readline().rstrip().split())
    house.append([R,G,B])

ans = sys.maxsize

for j in range(3):
    min_house = [[sys.maxsize,sys.maxsize,sys.maxsize] for _ in range(N)]
    min_house[0][j] = house[0][j]
    for i in range(1,N-1):
        for k in range(3):
            if k == 0:
                min_house[i][k] = house[i][k] + min(min_house[i-1][1],min_house[i-1][2]) 
            if k == 1:
                min_house[i][k] = house[i][k] + min(min_house[i-1][0],min_house[i-1][2]) 
            if k == 2:
                min_house[i][k] = house[i][k] + min(min_house[i-1][0],min_house[i-1][1])
    if j == 0:
        ans = min(ans,house[N-1][1] + min(min_house[N-2][0],min_house[N-2][2]),house[N-1][2] + min(min_house[N-2][0],min_house[N-2][1]))
    if j == 1:
        ans = min(ans,house[N-1][0] + min(min_house[N-2][1],min_house[N-2][2]),house[N-1][2] + min(min_house[N-2][0],min_house[N-2][1]))
    if j == 2:
        ans = min(ans,house[N-1][1] + min(min_house[N-2][0],min_house[N-2][2]),house[N-1][0] + min(min_house[N-2][1],min_house[N-2][2]))
    

print(ans) 

