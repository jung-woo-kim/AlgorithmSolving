import sys


N,K = map(int,sys.stdin.readline().rstrip().split())

li = sys.stdin.readline().rstrip()

stack = [li[0]]
cnt = 0

for i in range(1,N):

    
    while cnt < K and stack:
        if int(stack[-1]) < int(li[i]):
            temp = stack.pop()
            cnt+=1
        else:
            break

    stack.append(li[i])
    
if cnt != K:
    for _ in range(K - cnt):
        stack.pop()
   


print(''.join(stack))
