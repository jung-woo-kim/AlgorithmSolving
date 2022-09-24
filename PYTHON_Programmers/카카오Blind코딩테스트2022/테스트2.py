def solution(cap, n, deliveries, pickups):
    answer = 0
    now_delivery = cap
    now_pickups = 0

    while sum(deliveries) + sum(pickups) > 0:
        distance = -1
        
        now_pickups = 0

        #배달 출발
        if sum(deliveries) < cap:
            now_delivery = sum(deliveries)
        else:
            now_delivery = cap

        for i in range(n-1,-1,-1):
            if deliveries[i] > 0:
                distance = max(i,distance)
                #다 배달 가능하면
                if now_delivery - deliveries[i]> 0: 
                    now_delivery -= deliveries[i]
                    deliveries[i] = 0
                #다 배달 안되면
                else:
                    deliveries[i] -= now_delivery
                    now_delivery = 0

        for i in range(n-1,-1,-1):
            if pickups[i] > 0:
                distance = max(i,distance)
                if now_pickups+ pickups[i] <= cap:
                    now_pickups += pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= (cap-now_pickups)
                    now_pickups = cap

        answer += ((distance+1)*2)


    return answer

print(solution(4,5,[0,2,0,2,1],[2,0,2,2,1]))