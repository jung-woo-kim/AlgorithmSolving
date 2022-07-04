def solution(participant, completion):
    answer = ''
    
    dicp = dict()
    
    for p in participant:
        try:
            dicp[p] += 1
        except:
            dicp[p] = 1
    
    for c in completion:
        dicp[c] -= 1
    for p in participant:
        if dicp[p] > 0:
            answer = p
    return answer