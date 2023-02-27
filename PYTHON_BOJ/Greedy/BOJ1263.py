import sys

N = int(sys.stdin.readline().rstrip())

time = []

for _ in range(N):
    T, S = map(int,sys.stdin.readline().rstrip().split())
    time.append((T,S))


time.sort(reverse=True, key = lambda x: x[1])

# 현재 일이 끝난 시간
ans = time[0][1] - time[0][0]

for i in range(1,N):

    ## 현재 일을 최대한 늦게 시작한 시간이 i번째 일이 끝나야 하는 시간보다 늦다면
    ## 시작 시간이 i번째 일을 시작할 수 있는 가장 늦은 시간으로 갱신할 수 있다.
    if ans > time[i][1]:
        ans = time[i][1] - time[i][0]
    
    ## 현재 일을 최대한 늦게 시작한 시간이 i번째 일이 끝나야 하는 시간보다 빠르다면
    ## 현재 늦게 시작한 시간에서 걸리는 시간을 빼야한다.
    else:
        ans -= time[i][0]

print(ans if ans >= 0 else -1)