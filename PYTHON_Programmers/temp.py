import heapq

def solution(n, k, enemy):
    answer = 0
    hq = []

    for e in enemy:
        if e <= n:
            heapq.heappush(hq,(-e,e))
            n -= e
        else:
            heapq.heappush(hq,(-e,e))
            n-=e
            while k > 0 and hq:
                max = heapq.heappop(hq)[1]
                n += max
                k -= 1
                if n > 0:
                    break
            if n < 0:
                return answer
        answer += 1

    return answer