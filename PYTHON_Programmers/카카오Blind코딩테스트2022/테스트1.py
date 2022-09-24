def solution(today, terms, privacies):
    answer = []

    dic = dict()
    people = []
    y,m,d = today.split(".")
    now = int(y[2:]) * 28 *12 + int(m) *28 + int(d)
    for item in terms:
        pol,time = item.split()
        dic[pol] = int(time) *28
    
    for item in privacies:
        time,pol = item.split()
        y,m,d = time.split(".")
        effective_day = int(y[2:]) * 28 *12 + int(m) *28 + int(d) + dic[pol]
        people.append(effective_day)

    for i in range(len(people)):
        if people[i] <= now:
            answer.append(i+1)
    print(now)
    print(people)

    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
