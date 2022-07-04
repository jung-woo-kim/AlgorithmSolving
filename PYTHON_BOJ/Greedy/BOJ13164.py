import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

height = list(map(int,sys.stdin.readline().rstrip().split()))

diff = []
for i in (range(len(height)-1)):
    diff.append(abs(height[i] - height[i+1]))

diff.sort()

print(sum(diff[:len(diff)-(K-1)]))
