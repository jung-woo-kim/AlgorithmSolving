def solution(msg):
    answer = []
    dic = dict()

    for i in range(26):
        dic[chr(i+65)] = i+1

    idx = 0
    now = ""
    num = 27
    while idx < len(msg):
        now += msg[idx]
        try:
            dic[now]
        except:
            dic[now] = num
            answer.append(dic[now[:-1]])
            num += 1
            idx -= 1
            now = ""
        idx += 1
    answer.append(dic[now])
    return answer
solution("TOBEORNOTTOBEORTOBEORNOT")