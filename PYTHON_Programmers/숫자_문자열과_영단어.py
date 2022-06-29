def solution(s):
    answer = 0
    dic = dict()
    dic['zero'] = 0
    dic['one'] = 1
    dic['two'] = 2
    dic['three'] = 3
    dic['four'] = 4
    dic['five'] = 5
    dic['six'] = 6
    dic['seven'] = 7
    dic['eight'] = 8
    dic['nine'] = 9
    
    for st in dic.keys():
        if st in s:
            s = s.replace(st,str(dic[st]))
        
    answer = int(s)
    return answer

print(solution("one4seveneight"))