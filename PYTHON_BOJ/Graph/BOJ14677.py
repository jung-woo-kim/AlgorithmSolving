from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

drug = sys.stdin.readline().rstrip()

q = deque()

if drug[0] == "B":
    q.append(("L",1,N*3-1,1))

if drug[-1] == "B":
    q.append(("L",0,N*3-2,1))
answer = 0
while q:
    print(q)
    time,start,end,total = q.popleft()
    answer = max(answer,total)

    if start < end:
        
        if time == "B":
            if drug[start] == "B":
                q.append(("L",start+1,end,total+1))
            if drug[end] == "B":
                q.append(("L",start,end-1,total+1))
        elif time == "L":
            if drug[start] == "L":
                q.append(("D",start+1,end,total+1))
            if drug[end] == "L":
                q.append(("D",start,end-1,total+1))
        elif time == "D":
            if drug[start] == "D":
                q.append(("B",start+1,end,total+1))
            if drug[end] == "L":
                q.append(("B",start,end-1,total+1))
print(answer)