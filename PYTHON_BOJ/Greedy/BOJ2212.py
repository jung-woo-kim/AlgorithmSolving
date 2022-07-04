import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

location = list(map(int,sys.stdin.readline().rstrip().split()))

location.sort()

diff = []
for i in (range(len(location)-1)):
    diff.append(abs(location[i] - location[i+1]))

diff.sort()

print(sum(diff[:len(diff)-(K-1)]))
