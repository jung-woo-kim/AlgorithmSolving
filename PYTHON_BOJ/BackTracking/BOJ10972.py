import sys

N = int(sys.stdin.readline().rstrip())

permutation = sys.stdin.readline().rstrip()

permutation += " "
check = False
visited = [False for _ in range(N)]
answer = ""

def DFS(depth,now):
    global check
    global answer
    if depth == N:
        if check:
            answer = now
        if now == permutation:
            check = True
        return

    for i in range(1,N+1):
        if not visited[i-1]:
            visited[i-1] = True
            DFS(depth + 1,now+str(i)+" ")
            visited[i-1] = False
DFS(0,"")

if answer == "":
    print(-1)
else:
    print(answer)