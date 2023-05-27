def solution(keymap, targets):
    answer = []
    dic = dict()

    for key in keymap:
        for i,k in enumerate(key):
            if dic.get(k):
                if dic[k] > i+1:
                    dic[k] = i+1
            else:
                dic[k] = i+1
    print(dic)

    for t in targets:
        
        sum = 0
        try:
            for char in t:
                sum += dic[char]
            answer.append(sum)
        except:
            answer.append(-1)
    return answer