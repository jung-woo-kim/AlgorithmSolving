import sys

def get_walking_with_max(li):
    temp = 0
    for i in range(M,len(li),M):
        temp += abs(li[i])*2
    return temp

def get_walking_without_max(li):
    temp = 0
    for i in range(0,len(li),M):
        temp += abs(li[i])*2
    return temp

N,M = map(int,sys.stdin.readline().rstrip().split())

li = list(map(int,sys.stdin.readline().rstrip().split()))

li.sort()
minus = []
plus = []

for num in li:
    if num >= 0:
        plus.append(num)
    else:
        minus.append(num)
plus = sorted(plus,reverse=True)
answer = 0

if len(plus) == 0:
    answer += get_walking_with_max(minus)
    answer += abs(min(minus))
elif len(minus) == 0:
    answer += get_walking_with_max(plus)
    answer += abs(max(plus))
elif abs(max(plus)) < abs(min(minus)):
    answer += get_walking_with_max(minus)
    answer += get_walking_without_max(plus)
    answer += abs(min(minus))
else:
    answer += get_walking_with_max(plus)
    answer += get_walking_without_max(minus)
    answer += abs(max(plus))

print(answer)