def solution(n, lost, reserve):
    answer = 0
    people = [1 for _ in range(n+2)]
    people[0] = 0
    people[n+1] = 0
    
    for r in reserve:
        people[r] += 1
        
    
    for l in lost:
        people[l] -= 1
        
    for i in range(1,n+1):
        if people[i] == 0:
            if people[i-1] > 1:
                people[i] = 1
                people[i-1] -= 1
            elif people[i+1] > 1:
                people[i] = 1
                people[i+1] -= 1
            
    
    
    for i in range(1,n+1):
        if people[i] >= 1:
            answer+=1
    print(people)
    
    return answer