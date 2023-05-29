from collections import Counter
def solution(X, Y):
    answer = ''
    x = Counter(X)
    y = Counter(Y)

    for i in x:
        cnt = 0
        if i in y:
            cnt = min(x[i], y[i])
        for j in range(cnt):
            answer += i

    if answer == '':
        return "-1"
    else:
        answer = sorted(answer, reverse=True)
        if answer[0] == '0':
            return "0"

    return ''.join(answer)