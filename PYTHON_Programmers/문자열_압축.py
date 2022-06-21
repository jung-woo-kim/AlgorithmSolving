def solution(s):
    answer = len(s)
    str_len = 1
    
    while str_len <= len(s)//2:
        temp = 0
        li = []
        
        new_str = ""
        
        while temp < len(s):
            li.append(s[temp:temp+str_len])
            
            temp += str_len
        print(li)
            
        cont = 0
            
        for i in range(0,len(li)-1):
            
            if li[i] == li[i+1]:
                cont += 1
                if i == len(li)-2:
                    new_str = new_str + str(cont+1) + li[i]
            else:
                if cont == 0:
                    new_str += li[i]
                else:
                    new_str = new_str + str(cont+1) + li[i]

                if i == len(li)-2:
                    new_str += li[i+1]
                cont = 0
         

        print(new_str)
        answer = min(answer,len(new_str))

        str_len += 1
    
    return answer

print(solution("aaaaaaaaaa"))