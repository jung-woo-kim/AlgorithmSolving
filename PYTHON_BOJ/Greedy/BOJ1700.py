from collections import deque
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

item = list(map(int,sys.stdin.readline().rstrip().split()))
item = deque(item)
item_idx = [deque() for _ in range(K+1)]

now_multi = []
for i in range(K):
    item_idx[item[i]].append(i)

answer = 0

# print(item_idx)

for i in range(K):

    if item[i] in now_multi:
        item_idx[item[i]].popleft()
        continue

    if len(now_multi) < N:
        now_multi.append(item[i])
        item_idx[item[i]].popleft()
    else:
        
        temp = -1
        id = -1
        for m in now_multi:    
            if len(item_idx[m]) > 0:
                if temp < item_idx[m][0]:
                    temp = item_idx[m][0]
                    id = m
            else:#뒤에 나오지도 않음
                id = m
                break
 
        now_multi.remove(id)
        now_multi.append(item[i])
        item_idx[item[i]].popleft()
        answer += 1

print(answer)