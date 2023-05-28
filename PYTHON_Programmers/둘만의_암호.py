def solution(s, skip, index):
    answer = ''
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    for char in s:
        idx = ord(char) -97 
        count = 0
        plus = 0

        while count < index:
            plus += 1
            if alphabet_list[(idx + plus)%26] in skip:
                continue
            else:
                count += 1
        
        answer += alphabet_list[(idx + plus)%26]
            

    return answer