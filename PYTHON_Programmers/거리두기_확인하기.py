from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check_distance(place):
    q = deque()
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                q.append([x,y])
    print(q)
    for i in range(len(q)-1):
        for j in range(i+1,len(q)):
            x_1,y_1 = q[i]
            x_2,y_2 = q[j]
            if abs(x_1 - x_2) + abs(y_1 - y_2) <= 2:

                if abs(x_1 - x_2) + abs(y_1 - y_2) <= 1:
                    return 0
                if y_1 == y_2:
                   if x_1 > x_2 and place[x_1 - 1][y_1] != "X":
                        return 0
                   if x_1 < x_2 and place[x_2 - 1][y_1] != "X":
                        return 0
                elif x_1 == x_2:
                    
                    if y_1 > y_2 and place[x_1][y_1-1] != "X":
                        return 0
                    if y_1 < y_2 and place[x_2][y_2-1] != "X":

                        return 0
                else:
                    max_x = max(x_1,x_2)
                    max_y = max(y_1,y_2)
                    min_x = min(x_1,x_2)
                    min_y = min(y_1,y_2)
                    check = False
                    if place[min_x][min_y] == "X" and place[max_x][max_y] == "X":
                        check = True
                    
                    if place[min_x][max_y] == "X" and place[max_x][min_y] == "X":
                        check = True
                    
                    if not check:
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check_distance(place))

    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]])