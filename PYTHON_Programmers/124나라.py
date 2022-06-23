def solution(n):
    answer = ''
    li = []
    while n > 0:
        if n % 3 == 0:
            n = n//3-1
            li.append(4)
        elif n % 3 == 1:
            n = n//3
            li.append(1)
        else:
            n = n//3
            li.append(2)
        
    li.reverse()
        
    for st in li:
        answer += str(st)
    
    return answer

print(solution(4))