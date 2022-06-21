def solution(record):
    answer = []

    temp = dict()

    for str in record:
        li = str.split()
        if li[0] == "Enter" or li[0] == "Change":
            temp[li[1]] = li[2]

    for str in record:

        li = str.split()


        if len(li) == 2:
            answer.append(temp[li[1]]+"님이 나갔습니다.")
            continue

        if li[0] == "Enter":
            answer.append(temp[li[1]]+"님이 들어왔습니다.")


    return answer