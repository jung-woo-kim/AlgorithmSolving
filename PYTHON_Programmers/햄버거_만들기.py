def solution(ingredient):
    # 2 야채 1 빵 3 고기 1 2 3 1
    answer = 0

    wrapping = []

    for i in ingredient:
        wrapping.append(i)
        if len(wrapping) < 4:
            continue
        if wrapping[-1] == 1 and wrapping[-2] == 3 and wrapping[-3] == 2 and wrapping[-4] == 1:
            answer += 1
            wrapping.pop()
            wrapping.pop()
            wrapping.pop()
            wrapping.pop()
        
    return answer