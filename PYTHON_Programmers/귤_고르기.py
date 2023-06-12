from collections import Counter

def solution(k, tangerine):
    answer = 10000001
    count = Counter(tangerine).most_common()

    sum = 0
    total = 0
    for key,num in count:
        sum += num
        total += 1
        if sum >= k:
            answer = min(answer,total)
            sum = 0
            break

    return answer