import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))


arr_sum = [0]

for i in range(N):
    arr_sum.append(arr_sum[i] + arr[i])

right = 1
left = 0

now = arr_sum[right] - arr_sum[left]

answer = 0

while right < N+1 and left < right:

    
    if arr[right-1] > M:
        left = right
        right = right + 1
        continue

    now = arr_sum[right] - arr_sum[left]

    if now <= M:
        answer = max(answer,now)
        right += 1
    else:
        left += 1

   
print(answer)