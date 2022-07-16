import sys

N, K = map(int,sys.stdin.readline().rstrip().split())


# #antatica -> antic
# visited[0] = True
# visited[13] = True
# visited[19] = True
# visited[8] = True
# visited[2] = True

#print(ord('c')-97)

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
# print(li)
print(antatica)
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