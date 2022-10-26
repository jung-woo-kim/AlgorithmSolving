import sys

small = []

for _ in range(9):
    small.append(int(sys.stdin.readline().rstrip()))

def dfs(start,st,depth):
    if depth == 7:
        li = list(map(int,st.split()))
        s = 0
        tmp = []
        for i in li:
            s += small[i]
            tmp.append(small[i])
        if s == 100:
            tmp.sort()
            for t in tmp:
                print(t)
            exit()

    for i in range(start+1,9):
        dfs(i,st+str(i)+" ",depth+1)

dfs(-1,"",0)