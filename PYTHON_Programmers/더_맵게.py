import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    
    for s in scoville:
        heapq.heappush(hq,s)

    while hq[0] <= K:
        if(len(hq) == 1):
            answer = -1
            break
        else:
            answer += 1
        
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        heapq.heappush(hq,a + b*2)
        
        
    
    return answer