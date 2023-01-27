def solution(ingredient):
    answer = 0
    stack = []
    for item in ingredient:
        stack.append(item)
        if len(stack) >= 4:
            temp = stack[-5:-1]
            if is_hamburger(temp):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
    return answer

def is_hamburger(li):
    hamburger = [1,2,3,1]
    for i in range(4):
        if li[i] != hamburger[i]:
            return False
    
    return True