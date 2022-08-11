import sys

N, S = map(int,sys.stdin.readline().rstrip().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))


arr_sum = [0]

for i in range(N):
    arr_sum.append(arr_sum[i] + arr[i])

right = 1
left = 0

now = arr_sum[right] - arr_sum[left]
now_len = 1

answer = 1e9

while right < N+1 and left < right:

    now = arr_sum[right] - arr_sum[left]

    if now >= S:
        answer = min(answer,now_len)
        left += 1
        now_len -= 1
    else:
        right += 1
        now_len += 1

   


if answer == 1e9:
    print(0)
else:
    print(answer)