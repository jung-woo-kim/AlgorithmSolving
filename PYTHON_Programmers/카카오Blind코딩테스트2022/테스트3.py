from copy import copy

total = []

def DFS(emo,depth,end, emoticons,users):
    global total

    if depth == end:
        people = []
        end_money = 0
        for i in range(len(users)):
            sale,money = users[i]
            people_money = 0
            for e_sale,e_money in emo:
                if e_sale >= sale:
                    people_money += e_money
            
            end_money += people_money
            #넘어서면 이라며;;;;
            if people_money >= money:
                people.append(i+1)
                end_money -= people_money
        total.append((len(people),end_money))
        return

    for i in [10,20,30,40]:
        tmp = copy(emo)
        tmp.append((i,emoticons[depth]//100*(100-i)))
        DFS(tmp,depth+1,end,emoticons,users)
        

def solution(users, emoticons):
    answer = []
    DFS([],0,len(emoticons),emoticons,users)
    total.sort(key=lambda x:x[1],reverse=True)
    total.sort(reverse=True)
    return answer

solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])