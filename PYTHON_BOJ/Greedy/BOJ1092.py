import sys

N = int(sys.stdin.readline().rstrip())

crain = list(map(int,sys.stdin.readline().rstrip().split())) 

M = int(sys.stdin.readline().rstrip())

box = list(map(int,sys.stdin.readline().rstrip().split()))

box.sort(reverse=True)
crain.sort(reverse=True)


print(box)
print(crain)

answer = 0

if box[M-1] > crain[0]:
    print(-1)
    exit()

while len(box) > 0:
   
    for i in crain:
        for j in range(0,len(box)):
            if i >= box[j]:
                box.remove(box[j])
                break
    
    print(box)
    answer += 1

print(answer)