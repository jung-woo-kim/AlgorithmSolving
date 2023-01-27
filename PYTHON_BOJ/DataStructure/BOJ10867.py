import sys

N = int(sys.stdin.readline().rstrip())

li = list(set(list(map(int,sys.stdin.readline().rstrip().split()))))

li.sort()

print(*li)