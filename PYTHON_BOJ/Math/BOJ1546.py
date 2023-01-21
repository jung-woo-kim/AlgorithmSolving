import sys

N = int(sys.stdin.readline().rstrip())

score = list(map(int,sys.stdin.readline().rstrip().split()))

max_score = max(score)

total = 0

for s in score:
    total += s/max_score * 100

print(total/len(score))
