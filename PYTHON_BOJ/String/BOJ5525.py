import sys

N = int(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline().rstrip())

S = sys.stdin.readline().rstrip()

answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)