import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
recog_num = int(sys.stdin.readline().rstrip())
recog = list(map(int,sys.stdin.readline().rstrip().split()))

now = deque()

for i in range(recog_num):
    check = False
    
    for j in range(len(now)):
        if now[j][2] == recog[i]:
            now[j][1] += 1
            check = True
            break
    if check:
        continue

    if len(now) < N:
        now.append([i,1,recog[i]])
        continue
    
    

    min_list = []

    sorted_list = sorted(now,key=lambda x:x[1])
    min_recog = sorted_list[0][1]

    for s in sorted_list:

        if s[1] > min_recog:
            break
        min_list.append(s)

    now.remove(sorted(min_list,key=lambda x:x[0])[0])
    now.append([i,1,recog[i]])

   

s = ""
for i,rocog,stu in sorted(now,key=lambda x:x[2]):
    s += str(stu) + " "

print(s[:-1])