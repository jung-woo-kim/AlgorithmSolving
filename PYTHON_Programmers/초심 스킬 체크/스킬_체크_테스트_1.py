import math

def solution(w,h):
    answer = 1
    num = math.gcd(w,h)

    s_w = w // num
    s_h = h // num

    print(w*h - ((s_w * s_h -2) * num))

    return answer

solution(8,12)