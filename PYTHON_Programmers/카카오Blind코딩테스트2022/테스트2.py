def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    while pickups and pickups[-1] == 0:
        pickups.pop()

    while deliveries or pickups:
        answer += max(len(deliveries)*2, len(pickups)*2)

        box = 0

        while (deliveries and box <= cap):
            if deliveries[-1] + box <= cap:
                box += deliveries[-1]
            else:
                deliveries[-1] -= (cap-box)
                break 
            deliveries.pop()

        box = 0

        while (pickups and box <= cap):
            if pickups[-1] + box <= cap:
                box += pickups[-1]
            else:
                pickups[-1] -= (cap-box)
                break 
            pickups.pop()
        

    return answer

print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))