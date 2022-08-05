from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

def BFS():
    q = deque()
    q.append((N,[N]))
    visited = [False for _ in range(N+1)]
    visited[N] = True

    while q:
        n,n_li = q.popleft()
        if n == 1:
            return n , n_li
        if n%3 == 0:
            if n//3 > 0:
                if not visited[n//3]:
                    visited[n//3] = True
                    tmp = n_li[:]
                    tmp.append(n//3)
                    q.append((n//3,tmp))
            
        if n%2 == 0:
            if n//2 > 0:
                if not visited[n//2]:
                    visited[n//2] = True
                    tmp = n_li[:]
                    tmp.append(n//2)
                    q.append((n//2,tmp))
        if n-1 > 0:
            if not visited[n-1]:
                visited[n-1] = True
                tmp = n_li[:]
                tmp.append(n-1)
                q.append((n-1,tmp))

cnt,num = BFS()

print(len(num)-1)
answer = ""
for a in num:
    answer += str(a)+" "
print(answer)