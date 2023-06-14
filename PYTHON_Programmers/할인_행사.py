from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        check = True
        for j in range(len(want)):
            if c.get(want[j]) == None:
                check = False
                break
            if c.get(want[j]) < number[j]:
                check = False
                break
        if check:
            answer += 1
    return answer