import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    player = []
    for __ in range(11):
        player.append(list(map(int,sys.stdin.readline().rstrip().split())))

    visited = [False for __ in range(11)]
    result = 0
    def dfs(depth,n):
        global result
        if depth == 11:
            li = list(map(int,n.split()))
            sum = 0
            idx = 0
            for player_idx in li:
                sum += player[player_idx][idx]
                idx += 1
            result = max(result,sum)

        
        for i in range(11):
            if not visited[i]:
                if player[i][depth] != 0:
                    visited[i] = True
                    temp = n +str(i) + " "
                    dfs(depth+1,temp)
                    visited[i] = False
    
    dfs(0,"")
    print(result)