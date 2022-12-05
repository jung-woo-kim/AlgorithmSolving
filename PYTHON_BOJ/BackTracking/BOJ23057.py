import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
sum_all = sum(nums)
num = set()

def DFS(s,goal,now,depth):
    if depth == goal:
        li = now.split()
        sum = 0
        for i in li:
            sum += nums[int(i)]
        num.add(sum)
        return

    for i in range(s,N):
        temp = now
        temp += str(i) + " "
        DFS(i + 1,goal,temp,depth+1)

for goal in range(1,N+1):
    DFS(0,goal,"",0)

print(sum_all - len(num))
