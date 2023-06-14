def solution(cards):
    answer = []
    visited = [False for i in range(len(cards))]

    for i in range(len(cards)):
        temp = 1
        idx = i
        while visited[cards[idx]-1]:
            visited[cards[idx]-1] = True
            temp *= cards[idx]
            idx = cards[idx]
        answer.append(temp)
    answer.sort(reverse=True)
    print(answer)
    if len(answer) == 1:
        return 0
    return answer[0] * answer[1]