import sys

N = int(sys.stdin.readline().rstrip())


a = [False,False] + [True]*(N-1)
primes=[]

for i in range(2,N+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False

primes_sum = [0]

for i in range(len(primes)):
    primes_sum.append(primes_sum[i] + primes[i])

answer = 0
left = 0
right = 1

while left < right and right < len(primes)+1:
    now = primes_sum[right] - primes_sum[left]

    if now < N:
        right += 1
    elif now > N:
        left += 1
    else:
        answer += 1
        right += 1

print(answer)