import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

minus_list = []
plus_list = []

arr.sort()

# for a in arr:
#     if a < 0:
#         minus_list.append(a)
#     else:
#         plus_list.append(a)

# minus_list.sort(reverse=True)

# li = minus_list + plus_list


left = 0
right = N-1

standard = abs(arr[left] + arr[right])
answer = [arr[left],arr[right]]

while left < right:
    temp = arr[left] + arr[right]

    if standard > abs(temp):
        standard = abs(temp)
        answer = [arr[left],arr[right]]

    if temp < 0:
        left += 1
        
    elif temp > 0:
        right -= 1

    else:
        print(str(arr[left])+" "+str(arr[right]))
        exit()

   

print(str(answer[0])+" "+str(answer[1]))