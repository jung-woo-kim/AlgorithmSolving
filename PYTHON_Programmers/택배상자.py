
def solution(order):
    answer = 0
    sub_belt = []
    belt = [i for i in range(len(order),0,-1)]

    for o in order:
        print(belt)
        print(sub_belt)
        if belt:
            if belt[-1] == o:
                belt.pop()
                answer += 1
                continue
            if belt[-1] > o:
                if sub_belt and sub_belt[-1] == o:
                    sub_belt.pop()
                    answer += 1
                    continue
                else:
                    return answer
            while belt or sub_belt:
                sub_belt.append(belt.pop())

                if belt[-1] == o:
                    belt.pop()
                    answer += 1
                    break
            continue
        if not belt:
            if sub_belt and sub_belt[-1] == o:
                sub_belt.pop()
                answer += 1
                continue
            else:                    
                return answer
        
        

        


    return answer