import sys

from numpy import negative

N, M = map(int,sys.stdin.readline().rstrip().split())

edge = []
for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().rstrip().split())
    edge.append((A,B,C))

distance = [1e9 for _ in range(N+1)]

def belmanfod(start):
    distance[start] = 0

    for i in range(N):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(M):
            cur_node = edge[j][0]
            next_node = edge[j][1]
            edge_cost = edge[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != 1e9 and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1:
                    return True

    return False

negative_cycle = belmanfod(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == 1e9:
            print('-1')
        else:
            print(distance[i])