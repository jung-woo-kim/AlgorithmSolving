import sys

N, P = map(int,sys.stdin.readline().rstrip().split())

guitar = [[] for _ in range(6)]
answer = 0

for _ in range(N):
    line, pret = map(int,sys.stdin.readline().rstrip().split())
    while True:
        if guitar[line-1]:
            if guitar[line-1][-1] == pret:
                break
            elif guitar[line-1][-1] > pret:
                guitar[line-1].pop()
                answer += 1
            else:
                guitar[line-1].append(pret)
                answer += 1
        else:
            guitar[line-1].append(pret)
            answer += 1
            break

print(answer)