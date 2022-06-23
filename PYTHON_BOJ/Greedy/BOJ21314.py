import sys

minkyum = sys.stdin.readline()


cnt = 0
answer = ""
answer_min = ""

for st in minkyum:
    if st == "M":
        cnt +=1
    elif st == "K":
        if cnt == 0:
            answer += str(5)
            answer_min += str(5)
        else:
            answer += str(5*(pow(10,cnt)))
            answer_min += str(pow(10,cnt)+5)
            cnt = 0

if cnt != 0:
    answer += '1'*cnt
    cnt-=1
    answer_min += str((pow(10,cnt)))

print(answer)
print(answer_min)
