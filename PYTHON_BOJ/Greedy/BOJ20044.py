import sys

N = int(sys.stdin.readline().rstrip())

student = list(map(int,sys.stdin.readline().rstrip().split()))

student.sort()

G = []

for i in range(N):
    G.append(student[i]+student[-i-1])

print(min(G))