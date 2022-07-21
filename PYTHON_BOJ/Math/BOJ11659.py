import sys

N, M = list(map(int,sys.stdin.readline().rstrip().split()))

nums = list(map(int,sys.stdin.readline().rstrip().split()))
sum_li = [0 for i in range(N)]
sum_li[0] = nums[0]
for i in range(1,N):
    sum_li[i] = sum_li[i-1] + nums[i]

for _ in range(M):
    i,j = list(map(int,sys.stdin.readline().rstrip().split()))
    if i > 1:
        print(sum_li[j-1] - sum_li[i-2])
    else:
        print(sum_li[j-1])

