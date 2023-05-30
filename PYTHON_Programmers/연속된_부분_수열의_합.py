def solution(sequence, k):
    answer = [0,0]
    start = 0
    end = 0
    sum = sequence[start]
    min_len = 1000001

    while end < len(sequence):


        if start > end:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
            continue

        if sum < k:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
            continue

        if sum == k:
            if end - start < min_len:
                min_len = end - start
                answer[0] = start
                answer[1] = end
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
            continue

        if sum > k:
            sum -= sequence[start]
            start += 1

                   


    return answer

solution([2, 2, 2, 2, 2],6)