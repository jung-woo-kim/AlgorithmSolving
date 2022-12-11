import sys

N = int(sys.stdin.readline().rstrip())
local_money = list(map(int,sys.stdin.readline().rstrip().split()))
max_money = int(sys.stdin.readline().rstrip())

start = 1
end = max(local_money)

while start <= end:
    mid = (start + end)//2
    sum_money = 0
    for i in range(N):
        if local_money[i] >= mid:
            sum_money += mid
        else:
            sum_money += local_money[i]
            
    
    if sum_money > max_money:
        end = mid-1
    else:
        start = mid + 1

print(end)