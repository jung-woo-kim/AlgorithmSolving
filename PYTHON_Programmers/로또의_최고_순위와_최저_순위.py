def solution(lottos, win_nums):
    answer = []
    up = 0
    down = 0
    dic = dict()
    dic[6] = 1
    dic[5] = 2
    dic[4] = 3
    dic[3] = 4
    dic[2] = 5
    dic[1] = 6
    dic[0] = 6
    
    for l in lottos:
        if l != 0:
            if l in win_nums:
                up += 1
                down += 1
        else:
            up+=1
    
    answer.append(dic[up])
    answer.append(dic[down])
    
    return answer