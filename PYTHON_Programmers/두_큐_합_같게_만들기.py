from collections import deque

def solution(queue1, queue2):
    answer = -2
    q1s = sum(queue1)
    q2s = sum(queue2)
    limit = len(queue1) + len(queue2)
    count = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while q1s != q2s:
        if count > limit:
            return -1
        
        while q1s > q2s:
            tmp = queue1.popleft()
            queue2.append(tmp)
            q1s -= tmp
            q2s += tmp
            count += 1
        while q2s > q1s:
            tmp = queue2.popleft()
            queue1.append(tmp)
            q2s -= tmp
            q1s += tmp
            count += 1
        
    return count