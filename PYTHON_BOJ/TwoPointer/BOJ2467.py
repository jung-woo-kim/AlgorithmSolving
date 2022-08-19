import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

li.sort()

left = 0
right = N-1

zero = [li[left],li[right]]

while left < right:
    now = li[left] + li[right]

    if abs(now) < abs(zero[0] + zero[1]):
        zero[0] = li[left]
        zero[1] = li[right]
    
    if now < 0:
        left += 1
    elif now > 0:
        right -= 1
    else:
        zero[0] = li[left]
        zero[1] = li[right]
        print(*zero)
        exit()
    
    

print(*zero)