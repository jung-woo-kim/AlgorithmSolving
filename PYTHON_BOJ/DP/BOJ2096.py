from copy import copy
import sys

N = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(N):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())

    arr.append([a,b,c])

max_dp = [arr[0][0],arr[0][1],arr[0][2]]
max_tmp = [arr[0][0],arr[0][1],arr[0][2]]

min_dp = [arr[0][0],arr[0][1],arr[0][2]]
min_tmp = [arr[0][0],arr[0][1],arr[0][2]]

for i in range(1,N):
    for j in range(0,3):
        if j == 0:
            max_dp[j] = arr[i][j] + max(max_tmp[0],max_tmp[1])
            min_dp[j] = arr[i][j] + min(min_tmp[0],min_tmp[1])
        if j == 1:
            max_dp[j] = arr[i][j] + max(max_tmp[0],max_tmp[1],max_tmp[2])
            min_dp[j] = arr[i][j] + min(min_tmp[0],min_tmp[1],min_tmp[2])
        if j == 2:
            max_dp[j] = arr[i][j] + max(max_tmp[2],max_tmp[1])
            min_dp[j] = arr[i][j] + min(min_tmp[2],min_tmp[1])
        
    max_tmp = copy(max_dp)
    min_tmp = copy(min_dp)

print(str(max(max_dp))+" "+str(min(min_dp)))
