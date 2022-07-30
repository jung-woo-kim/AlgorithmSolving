import sys

N = int(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline().rstrip())
if M != 0:
    broken = list(map(int,sys.stdin.readline().rstrip().split()))
else:
    broken = []

b_li = [0,0,0,0,0,0,0,0,0,0]

for b in broken:
    b_li[b] = 1

st = str(N)

case = [[] for _ in range(len(st))]

total = 1

for i in range(len(st)):
    for j in range(0,10):
        if j == int(st[i]):
            if b_li[j] == 0:
                case[i].append(j)
          
            for k in range(j-1,-20,-1):
                k %= 10
                if b_li[k] == 0:
                    case[i].append(k)
                    break
            for k in range(j+1,20):
                k %= 10
                if b_li[k] == 0:
                    case[i].append(k)
                    break
                  

            break

li = []

if len(case[0]) == 3:
    li.append(str(case[0][0]))
    li.append(str(case[0][1]))
    li.append(str(case[0][2]))
elif len(case[0]) == 2:
    li.append(str(case[0][0]))
    li.append(str(case[0][1]))
else:
    li.append(str(case[0][0]))



for i in range(1,len(case)):
    temp = []
    for j in range(len(li)):
        if len(case[i]) == 3:
            temp.append(li[j] + str(case[i][0]))
            temp.append(li[j] + str(case[i][1]))
            temp.append(li[j] + str(case[i][2]))
        elif len(case[i]) == 2:
            temp.append(li[j] + str(case[i][0]))
            temp.append(li[j] + str(case[i][1]))
        else:
            temp.append(li[j] + str(case[i][0]))
      
    li = temp

li.append('100')
li.append(str(10**len(str(N))))
if len(str(N)) > 1:
    li.append(str(10**(len(str(N))-1)))

print(li)

answer = [0 for _ in range(len(li))]
for i in range(len(li)):
    if li[i] == '100':
        answer[i] = abs(N-100)
    else:
        answer[i] = len(li[i])
        answer[i] += abs(int(li[i])-N)


print(min(answer))    




