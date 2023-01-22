import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

A = list(map(int,sys.stdin.readline().rstrip().split()))

robot = [False for _ in range(len(A))]

up_idx = 0
down_idx = N-1

def rotate_belt():
    global A
    global robot
    A = [A[-1]] + A[:len(A)-1]
    robot = [robot[-1]] + robot[:len(A)-1]
    if robot[down_idx]:
        robot[down_idx] = False

def move_robot():
    for i in range(N-2,-1,-1):
        if robot[i] and A[i+1] > 0 and not robot[i+1]:
            robot[i] = False
            robot[i+1] = True
            A[i+1] -= 1
    if robot[down_idx]:
        robot[down_idx] = False
    

def up_robot():
    if A[up_idx] > 0:
        A[up_idx] -= 1
        robot[up_idx] = True 

def check():
    temp = 0
    for a in A:
        if a == 0:
            temp += 1
    
    if temp >= K:
        return False
    return True

answer = 1
while True:

    rotate_belt()
    move_robot()
    up_robot()
    if not check():
        break

    answer += 1

print(answer)