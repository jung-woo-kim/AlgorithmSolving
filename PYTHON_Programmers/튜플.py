def solution(s):
    answer = []
    
    li = []
    idx = 1
    while idx<len(s)-1:
        tmp = ""
        if s[idx] == "{":
            idx += 1
            while True:
                if s[idx] == "}":
                    break
                tmp += s[idx]
                idx += 1
            li.append(tmp.split(","))
        idx += 1
    
    li.sort(key=lambda x: len(x))
    
    for items in li:
        for item in items:
            if int(item) not in answer:
                answer.append(int(item))    

    return answer