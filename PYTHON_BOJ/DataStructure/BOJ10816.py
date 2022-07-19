import sys
 
N = int(sys.stdin.readline().strip())

dic = dict()
nums = list(map(int,sys.stdin.readline().strip().split()))

for i in range(N):
    try:
        dic[nums[i]] += 1
    except:
        dic[nums[i]] = 1

M = int(sys.stdin.readline().strip())

answer = []
check = list(map(int,sys.stdin.readline().strip().split()))

for i in range(M):
    try:
        answer.append(str(dic[check[i]]))
    except:
        answer.append("0")

print(" ".join(answer))