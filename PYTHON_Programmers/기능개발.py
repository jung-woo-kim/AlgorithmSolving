def solution(progresses, speeds):
    answer = []
    total = 0
    
    progresses.reverse()
    speeds.reverse()
    
    while True:
        temp = 0
        for i in range(len(progresses)-1, -1, -1):
            progresses[i] = progresses[i]+speeds[i]
        
        
        for i in range(len(progresses)-1, -1, -1):
            if progresses[i] >= 100:
                progresses.pop()
                temp += 1
                total += 1
            else:
                break
            
            
        if temp > 0:
            answer.append(temp)
        if total == len(speeds):
            break
        
    return answer