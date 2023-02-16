import sys

N = int(sys.stdin.readline().rstrip())
dic = dict()
out = []

for i in range(N):
    dic[sys.stdin.readline().rstrip()] = i

for _ in range(N):
    out.append(sys.stdin.readline().rstrip())

answer = 0

for i in range(N-1):
    for j in range(i+1,N):
        if dic[out[i]] > dic[out[j]]:
            answer += 1
            break
print(answer)