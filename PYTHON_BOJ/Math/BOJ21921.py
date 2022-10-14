import sys

N,X = map(int,sys.stdin.readline().rstrip().split())

li = list(map(int,sys.stdin.readline().rstrip().split()))

value = sum(li[:X])

answer = value
answer_due = 1

for i in range(X,N):
    value += li[i]
    value -= li[i-X]

    if value > answer:
        answer = value
        answer_due = 1
    elif value == answer:
        answer_due += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(answer_due)