import sys
from itertools import combinations

n, l, r, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(2, n + 1):
    for comb in combinations(arr, i):
        if l <= sum(comb) <= r:
            if max(comb) - min(comb) >= x:
                result += 1

print(result)