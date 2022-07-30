import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

li = []
answer = 0
antatica = 0

visited = [False for _ in range(26)]
antic = ['a','n','t','i','c']

for w in antic:
    visited[ord(w) -97] = True

for _ in range(N):
    word = sys.stdin.readline().rstrip()[4:-4]
    word = set(list(word)) - set(antic)
    li.append(word)


def dfs(depth,s,n):
    global answer
    if depth == K-5:
        
        teach = set(list(n))
        temp = 0
        for w in li:
            t = w - teach
            if len(t) == 0:
                temp += 1
        answer = max(answer,temp)
        return
    
    for i in range(s,26):
        if not visited[i]:
            visited[i] = True
            temp = n+chr(i+97)
            dfs(depth + 1,i,temp)
            visited[i] = False

if K >= 5:
    dfs(0,0,"")
    print(answer)

if K < 5:
    print(0)
