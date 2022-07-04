def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    dic = dict()
    dic[1] = [1,1]
    dic[2] = [2,1]
    dic[3] = [3,1]
    dic[4] = [1,2]
    dic[5] = [2,2]
    dic[6] = [3,2]
    dic[7] = [1,3]
    dic[8] = [2,3]
    dic[9] = [3,3]
    dic['*'] = [1,4]
    dic[0] = [2,4]
    dic['#'] = [3,4]
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer+='L'
            left = num
        elif num == 3 or num == 6 or num == 9:
            answer+='R'
            right = num
        else:
            rx,ry = dic[right]
            lx,ly = dic[left]
            nx,ny = dic[num]
            if (abs(rx - nx)+abs(ry - ny)) < (abs(lx - nx)+abs(ly - ny)):
                answer+='R'
                right = num
            elif (abs(rx - nx)+abs(ry - ny)) == (abs(lx - nx)+abs(ly - ny)):
                if hand == "right":
                    answer+='R'
                    right = num
                else:
                    answer+='L'
                    left = num
            else:
                answer+='L'
                left = num   
    return answer