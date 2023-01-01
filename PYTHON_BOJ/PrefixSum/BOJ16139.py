import sys

S = sys.stdin.readline().rstrip()


temp = dict()

for i in range(97,124):
    temp[chr(i)] = 0

s_sum = [temp.copy() for i in range(len(S)+1)]

for i in range(1,len(S)+1):
    s_sum[i] = s_sum[i-1].copy()
    s_sum[i][S[i-1]] += 1
   

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    s,l,r = sys.stdin.readline().rstrip().split()

    print(s_sum[int(r)+1][s] - s_sum[int(l)][s])
    


