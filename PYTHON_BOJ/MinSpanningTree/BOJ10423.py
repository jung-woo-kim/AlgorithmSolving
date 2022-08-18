import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split())

power = list(map(int,sys.stdin.readline().rstrip().split()))

cable = []

for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    cable.append((w,u,v))

cable.sort()

city = [i for i in range(N+1)]

def find(x):
    if city[x] != x:
        city[x] = find(city[x])
    return city[x]

answer = 0

for w,u,v in cable:
    u_parent = find(u)
    v_parent = find(v)
    check_u = False
    check_v = False
    if u_parent != v_parent:

        if u_parent in power:
            check_u = True
        if v_parent in power:
            check_v = True
        
        if check_u and check_v:
            pass
        elif check_u:
            city[v_parent] = u_parent
            answer += w
        elif check_v:
            city[u_parent] = v_parent
            answer += w
        else:
            city[u_parent] = v_parent
            answer += w

print(answer)