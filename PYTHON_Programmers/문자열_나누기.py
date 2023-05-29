def solution(s):
    answer = 0
    x = ""
    x_num = 0
    x_diff_num = 0
    for i in range(len(s)):
        if x_diff_num == 0 and x_num == 0:
            x = s[i]
            x_num += 1
            continue
        
        if x != s[i]:
            x_diff_num += 1
        else:
            x_num += 1
        
        if x_num == x_diff_num:
            x_num = 0
            x_diff_num = 0
            answer += 1
    
    if not (x_diff_num == 0 and x_num == 0):
        answer += 1 
    return answer