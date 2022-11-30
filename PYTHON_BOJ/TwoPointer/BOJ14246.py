import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int,sys.stdin.readline().rstrip().split()))
k = int(sys.stdin.readline().rstrip())

sum = [0 for _ in range(n+1)]

for i in range(1,n+1):
    sum[i] = sum[i-1] + num[i-1]

start = 0
end = 1
answer = 0

while True:
    if end > n:
        break

    if sum[end] - sum[start] > k:
        answer += n-end+1
        start += 1
        end = start + 1
    else:
        end += 1
    
print(answer)