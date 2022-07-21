import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

li = []
alpha = []
answer = 0
antatica = 0

li = [set(input())-{'a','n','t','i','c'} for _ in range(N)]

alpha = set()
for word in li:
    for s in word:
        alpha.add(s)

alpha = list(alpha)
alpha.sort()

def dfs(depth,n,s):
    global answer

    if depth == K-5:
        print(n)
        temp = antatica
        for word in li:
            if word in n:
                temp +=1
        answer = max(answer,temp)
        return

    for i in range(s,len(alpha)):
        temp = n+alpha[i]
        dfs(depth+1,temp,i+1)

if len(alpha) <= K-5:
    print(N)
    exit()

if K < 5:
    print(0)
    exit()

if K == 5:
    print(antatica)
    exit()

dfs(0,"",0)
print(answer)