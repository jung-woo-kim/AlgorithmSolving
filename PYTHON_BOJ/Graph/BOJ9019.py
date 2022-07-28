from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())



def numToStr(A):
    temp = str(A)
    if A >= 1000:
        return temp
    elif 1000 > A >= 100:
        return "0"+temp
    elif 100 > A >= 10:
        return "00"+temp
    elif 10 > A > 0:
        return "000"+temp
    else:
        return "0000"


def D(A):
    num = int(A)
    temp = num*2
    if temp < 10000:
        return numToStr(temp)
    else:
        return numToStr(temp % 10000)

def S(A):
    num = int(A)
    temp = num-1
    if temp == -1:
        temp = 9999
    return numToStr(temp)

def L(A):
    num = int(A)
    temp_left = num//1000
    temp_right = num % 1000

    temp_right = numToStr(temp_right)
    return temp_right[1:] + str(temp_left)

def R(A):
    num = int(A)
    temp_left = num//10
    temp_right = num % 10

    temp_left = numToStr(temp_left)
    return str(temp_right)+temp_left[1:]

## 매개변수 모두 str
def BFS(n,goal):
    q = deque()
    q.append((numToStr(n),""))
    visited[n] = True
    while q:
        now,past = q.popleft()
        for i in range(4):
            if i == 0:
                temp = D(now)
                if not visited[int(temp)]:
                    visited[int(temp)] = True
                    q.append((temp,past+"D"))
                    if temp == goal:
                        print(past+"D")
                        return
            elif i == 1:
                temp = S(now)
                if not visited[int(temp)]:
                    visited[int(temp)] = True
                    q.append((temp,past+"S"))
                    if temp == goal:
                        print(past+"S")
                        return
            elif i == 2:
                temp = L(now)
                if not visited[int(temp)]:
                    visited[int(temp)] = True
                    q.append((temp,past+"L"))
                    if temp == goal:
                        print(past+"L")
                        return
            elif i == 3:
                temp = R(now)
                if not visited[int(temp)]:
                    visited[int(temp)] = True
                    q.append((temp,past+"R"))
                    if temp == goal:
                        print((past+"R"))
                        return

                


for _ in range(T):
    visited = [False for i in range(10000)]
    A, B = map(int,sys.stdin.readline().rstrip().split())
    BFS(A,numToStr(B))
