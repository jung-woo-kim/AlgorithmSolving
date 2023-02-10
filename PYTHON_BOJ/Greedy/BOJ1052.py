import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

answer = 0

while N > 0:

    if K == 1:
        j = 0
        while True:
            if N <= 2**j:
                answer += (2**j - N)
                break
            j+=1
        break
    
    i = 0
    while True:
        if N < 2**i:
            N -= 2**(i-1)
            K-=1
            break
        i+=1

print(answer)