import sys

N, K = map(int,sys.stdin.readline().rstrip().split())
li = list(map(int,sys.stdin.readline().rstrip().split()))

if N == K:
    print(sum(li))
    exit()
    
start = 0
end = K

sum_li = [0 for _ in range(N+1)]

for i in range(1,N+1):
    sum_li[i] = sum_li[i-1] + li[i-1]
print(sum_li)
answer = sum_li[end] - sum_li[start]

while end < N+1:
    temp = sum_li[end] - sum_li[start]

    answer = max(answer, temp)

    start += 1
    end += 1

print(answer)