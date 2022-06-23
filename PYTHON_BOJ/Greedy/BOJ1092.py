import sys

N = int(sys.stdin.readline().rstrip())

crain = list(map(int,sys.stdin.readline().rstrip().split())) 

M = int(sys.stdin.readline().rstrip())

box = list(map(int,sys.stdin.readline().rstrip().split()))

crain.sort()
crain.reverse()
box.sort()

boxSize = len(box)
#print(box[len(box)-1])

answer = 0

while box:
    check = False
    for i in crain:
        if boxSize != 0:
            if i > box[boxSize-1]:
                check = True
                box.pop()
                boxSize -= 1
    
    if not check:
        answer = -1
        break
    
    answer += 1

print(answer)