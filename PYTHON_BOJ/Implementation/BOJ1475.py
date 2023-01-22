import sys


N = sys.stdin.readline().rstrip()

li = [0 for i in range(10)]

for n in N:
    li[int(n)] += 1

max_num = 0
answer = 0
six_nine = 0

for i in range(0,10):
    if i != 6 and i != 9:
        answer = max(answer,li[i])
    else:
        six_nine += li[i]

if six_nine % 2 == 0:
    six_nine = six_nine // 2
else:
    six_nine = six_nine // 2 +1

print(max(six_nine,answer))