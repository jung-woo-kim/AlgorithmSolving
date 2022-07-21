import sys

N,M = list(map(int,sys.stdin.readline().rstrip().split()))

dic = dict()

for _ in range(N):
    site,password = sys.stdin.readline().rstrip().split()
    dic[site] = password

for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])