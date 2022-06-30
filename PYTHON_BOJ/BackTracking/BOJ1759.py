import sys

L,C = map(int,sys.stdin.readline().rstrip().split())

Alphabet = sys.stdin.readline().rstrip().split()
Alphabet.sort()
## i -> 지금까지 몇번 함수 들어왔는지

count = 0

visit = [False for _ in range(C)]


def dfs(s,password):
    if len(password) == L:
        vo = 0
        co = 0
        for i in range(L):
            if password[i] in 'aeiou': 
                vo += 1
            else: 
                co += 1
        if vo > 0 and co >1:
            print(password)
        
        return

    for i in range(s,C):
        if not visit[i]:
            visit[i] = True
            temp = password + Alphabet[i]
            dfs(i,temp)
            visit[i] = False

dfs(0,"")