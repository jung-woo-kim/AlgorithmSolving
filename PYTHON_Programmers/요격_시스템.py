def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])
    # max(targets)
    bomb = 0

    for t in targets:
        if t[0] < bomb:
            pass
        if t[0] >= bomb:
            bomb = t[1]
            answer += 1
        print(bomb)
    return answer