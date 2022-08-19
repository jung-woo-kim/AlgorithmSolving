import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

arr.sort()

left = 0
right = N-1

standard = abs(arr[left] + arr[right] + arr[1])
answer = [arr[left],arr[1],arr[right]]

for i in range(1,N-1):
    left = 0
    right = N-1
    
    while left < right and left < i and right > i:
        temp = arr[left] + arr[right] + arr[i]

        if standard > abs(temp):
            standard = abs(temp)
            answer = [arr[left],arr[i],arr[right]]

        if temp < 0:
            left += 1
            
        
        elif temp > 0:
            right -= 1

        else:
            print(*answer)
            exit()


   

print(*answer)