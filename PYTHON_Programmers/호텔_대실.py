import heapq

def solution(book_time):
    answer = 0
    hq = []

    for i in range(len(book_time)):
        hh,mm = book_time[i][0].split(":")
        start = int(hh) * 60 + int(mm)
        hh,mm = book_time[i][1].split(":")
        end = int(hh) * 60 + int(mm)
        book_time[i] = [start,end]
    
    book_time.sort(key=lambda x:x[0])
    
    sum = 1
    min_end = book_time[0][1]
    heapq.heappush(hq,book_time[0][1])
    for i in range(1,len(book_time)):
        if book_time[i][0] < min_end + 10:
            sum += 1
        else:
            heapq.heappop(hq)
        heapq.heappush(hq,book_time[i][1])
        min_end = hq[0]
        answer = max(answer,len(hq))
    return answer

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])