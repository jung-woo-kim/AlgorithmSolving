def solution(survey, choices):
    answer = ''
    dicts = {'T' : 0, 'R' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}

    for i in range(len(survey)):
        if choices[i] > 4:
            dicts[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dicts[survey[i][0]] += 4 - choices[i]

    answer += 'R' if dicts['R'] >= dicts['T'] else 'T'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'
    
    return answer