import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

li = []
alpha = []
answer = 0
antatica = 0
for _ in range(N):
    word = sys.stdin.readline().rstrip()[4:-4]
    
    word = list(set(list(word)))
    word.sort()
    temp = []
    for w in word:
        if w not in 'antic':
            temp.append(w)
            alpha.append(w)
    if len(temp) == 0:
        antatica += 1
    else:
        temp.sort()
        li.append("".join(temp))

alpha = list(set(alpha))
alpha.sort()

print(alpha)

visited = [False for i in range(len(alpha))]

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