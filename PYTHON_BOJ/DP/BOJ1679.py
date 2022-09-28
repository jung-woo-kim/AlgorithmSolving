import sys

N = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().rstrip().split()))

K = int(sys.stdin.readline().rstrip())

dp = [[]for _ in range(K+1)]
li = [0 for _ in range(nums[-1]*K + 1)]
for n in nums:
    dp[1].append(n)
    li[n] = 1

for i in range(2,K+1):
    for n in dp[i-1]:
        for num in nums:
            li[n+num] = 1
            dp[i].append(n+num)
    dp[i] = list(set(dp[i]))

for i in range(1,len(li)):
    if li[i] == 0:
        if i%2 == 0:
            print("holsoon win at "+str(i))
            exit()
        else:
            print("jjaksoon win at "+str(i))
            exit()