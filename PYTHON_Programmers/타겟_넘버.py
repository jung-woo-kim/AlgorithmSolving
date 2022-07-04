def solution(numbers, target):
    count = 0
    def dfs(i, sign, summation):
        nonlocal count
        if i==len(numbers):
            if summation == target:
                count = count + 1
            return

        summation = summation + numbers[i]*sign
        dfs(i+1,  1, summation)
        dfs(i+1, -1, summation)

    for sign in [-1, 1]:
        dfs(0, sign, 0)

    return count/2