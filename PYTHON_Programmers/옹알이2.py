def solution(babbling):
    answer = 0

    for b in babbling:
        idx = 0
        temp = ""
        check = False
        while idx < len(b):
            if b[idx:idx+2] == "ye":
               temp += "!"
               idx += 2 
            elif b[idx:idx+2] == "ma":
                temp += "@"
                idx += 2 
            elif b[idx:idx+3] == "aya":               
                temp += "#"
                idx += 3 
            elif b[idx:idx+3] == "woo":
                temp += "$"
                idx += 3
            else:
                check = True
                break
        
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                check = True
        
        if not check:
            continue
        
        answer += 1

    return answer