def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        print(number)
        print(answer)
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number

        stack.append(idx)

    return answer

solution([2, 3, 3, 5])