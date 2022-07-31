import sys

N = int(sys.stdin.readline().rstrip())

li = [[]for _ in range(10)]
word_li = []
dic = dict()
dic_important = dict()
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    word_li.append(word)
    idx = 0
    for i in range(len(word)-1,-1,-1):
        li[i].append(word[idx])
        try:
            dic_important[word[idx]] += 10**i
        except:
            dic_important[word[idx]] = 10**i
        
        idx += 1

now_num = 9 

important = sorted(dic_important.items(),key=lambda x: x[1], reverse=True)

for k,value in important:
    try:
        dic[k] += 0
    except:
        dic[k] = now_num
        now_num -= 1


# for i in range(len(li)-1,-1,-1):
#     temp = 0
#     for j in range(len(li[i])):
#         if temp < dic_important[li[i][j]]:
#             temp = dic_important[li[i][j]]


#         try:
#             dic[li[i][j]] += 0
#         except:
#             dic[li[i][j]] = now_num
#             now_num -= 1

answer = 0

for word in word_li:
    temp = ""
    for w in word:
        temp += str(dic[w])
    answer += int(temp)

print(answer)