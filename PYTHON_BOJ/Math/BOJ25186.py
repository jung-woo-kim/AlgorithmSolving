import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))


check = True
num = sum(li)

if num // 2 >= max(li):
    print("Happy")
else:
    print("Unhappy")