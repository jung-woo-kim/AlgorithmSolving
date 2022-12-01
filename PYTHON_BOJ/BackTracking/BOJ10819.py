import sys

N = int(sys.stdin.readline().rstrip())

array = list(map(int,sys.stdin.readline().rstrip().split()))

def calculater(li):
    sum = 0
    for i in range(len(li)-1):
        sum += abs(li[i] - li[i+1])
    return sum

visited = [False for i in range(N)]
answer = 0
def DFS(depth,before,sum):
    global answer
    if depth == N-1:
        answer = max(answer,sum)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            temp = sum
            print(sum)
            print(before)
            if before != -101:
                temp += abs(before - array[i])
                before = array[i]
            else:
                before = array[i]
            DFS(depth + 1, before, temp)
            visited[i] = False

DFS(0,-101,0)
print(answer)