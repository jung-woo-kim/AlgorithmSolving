import sys

TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    edges = []
    N,M,W = map(int,sys.stdin.readline().rstrip().split())
    for m in range(M):
        S,E,T = map(int,sys.stdin.readline().rstrip().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    for w in range(W):
        S,E,T = map(int,sys.stdin.readline().rstrip().split())
        edges.append((S,E,-T))
    
    distance = [1e9 for _ in range(N+1)]

    def belmanfod(start):
        distance[start] = 0

        for i in range(N):
            for j in range(M*2+W):
                cur_node = edges[j][0]
                next_node = edges[j][1]
                cost = edges[j][2]

                if distance[cur_node] != 1e9 and distance[next_node] > distance[cur_node] + cost:
                    distance[next_node] =  distance[cur_node] + cost
                    if i == N-1:
                        return True
        return False
    
    if belmanfod(1):
        print("YES")
    else:
        print("NO")
                    



