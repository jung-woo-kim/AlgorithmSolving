def solution(cards):
    answer = []
    visited = [False for i in range(len(cards))]

    for i in range(len(cards)):
        temp = 0
        idx = i
        while not visited[cards[idx]-1]:
            visited[cards[idx]-1] = True
            temp += 1
            idx = cards[idx] -1
        if temp != 0:
            answer.append(temp)
    answer.sort(reverse=True)
    if len(answer) == 1:
        return 0
    return answer[0] * answer[1]