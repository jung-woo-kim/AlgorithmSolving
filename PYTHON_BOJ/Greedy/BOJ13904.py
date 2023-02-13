import sys

N = int(sys.stdin.readline().rstrip())

homework = []

for _ in range(N):
    d,w = map(int,sys.stdin.readline().rstrip().split())
    homework.append((w,d))

homework.sort(reverse=True)

task = [0 for _ in range(1001)]

for score,day in homework:
    if task[day] == 0:
        task[day] = score
    else:
        while day != 1:
            day -= 1
            if task[day] == 0:
                task[day] = score
                break

print(sum(task))