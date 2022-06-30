import sys

N,M =  map(int,sys.stdin.readline().rstrip().split())

city = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

visited = [False for _ in range(len(chicken))]

##print(chicken)

result = 1e9

def dfs(depth,idx,s):

    global result

    if depth == M:
        temp = 0
        li = list(map(int,idx.split()))
        for h in house:
            chi_len = 1e9
            for j in range(M):
                chi_len = min(chi_len, abs(h[0] - chicken[li[j]][0]) + abs(h[1] - chicken[li[j]][1]))
            temp += chi_len
        result = min(result,temp)

        return
    
    for i in range(s,len(chicken)):
        #print(i)
        if not visited[i]:
            visited[i] = True
            temp = idx + str(i)+" "
         
            
            dfs(depth+1,temp,i+1)

            visited[i] = False

dfs(0,"",0)
print(result)