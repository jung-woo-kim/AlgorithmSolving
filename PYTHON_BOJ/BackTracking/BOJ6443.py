import sys

N = int(sys.stdin.readline().rstrip())

dic= dict()

visited = []
answer = set()

def dfs(depth,n,str):

    if depth == len(str):
        answer.add(n)
        return
            

    for i in range(len(str)):
        if not visited[i]:
            visited[i] = True
            temp = n + str[i]
            dfs(depth+1,temp,str)
            visited[i] = False


for _ in range(N):
    st = sys.stdin.readline().rstrip()
    visited = [False for i in range(len(st))]
    answer = set()
    # st = list(st)
    # st.sort()
    # st = "".join(st)
    dfs(0,"",st)
    answer = sorted(list(answer))

    for a in answer:
        print(a)
    
