from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    
    for i in range(0,len(cities)):
        if len(cache) < cacheSize:
            check = False
            for j in range(len(cache)):
                if cache[j] == cities[i].upper():
                    cache.remove(cities[i].upper())
                    cache.append(cities[i].upper())
                    answer += 1
                    check = True
                    break
            if not check:
                answer += 5
                cache.append(cities[i].upper())
        else:
            check = False
            for j in range(cacheSize):
                if cache[j] == cities[i].upper():
                    cache.remove(cities[i].upper())
                    cache.append(cities[i].upper())
                    answer += 1
                    check = True
                    break
            if not check:
                answer += 5
                cache.append(cities[i].upper())
                cache.popleft()
    

    
    return answer