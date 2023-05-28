def solution(id_list, report, k):
    answer = []
    rep = set()

    for r in report:
        rep.add(r)
    
    user_report = dict()
    user_reported = dict()

    for id in id_list:
        user_reported[id] = 0
        user_report[id] = []
    
    for r in rep:
        report_user, reported_user = r.split()
        user_reported[reported_user] += 1
        user_report[report_user].append(reported_user)

    for id in id_list:
        sum = 0
        for reported_user in user_report[id]:
            if user_reported[reported_user] >= k:
                sum += 1
        answer.append(sum)

    return answer