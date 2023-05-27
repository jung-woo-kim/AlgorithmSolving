def solution(n, m, section):
    answer = 0

    temp = 0

    for s in section:
        if s > temp:
            answer += 1
            temp = s+m-1
    
    return answer