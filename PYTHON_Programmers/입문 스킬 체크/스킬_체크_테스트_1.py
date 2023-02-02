import sys

def solution(survey, choices):
    answer = ''
    emotion = dict()

    emotion["A"] = 0
    emotion["N"] = 0
    emotion["C"] = 0
    emotion["F"] = 0
    emotion["M"] = 0
    emotion["J"] = 0
    emotion["R"] = 0
    emotion["T"] = 0

    for i in range(len(survey)):

        if choices[i] == 7:
            emotion[survey[i][1]] += 3    
        if choices[i] == 6:
            emotion[survey[i][1]] += 2
        if choices[i] == 5:
            emotion[survey[i][1]] += 1
        if choices[i] == 3:
            emotion[survey[i][0]] += 1
        if choices[i] == 2:
            emotion[survey[i][0]] += 2
        if choices[i] == 1:
            emotion[survey[i][0]] += 3

    answer = ""

    if emotion["R"] >= emotion["T"]:
        answer += "R"
    else:
        answer += "T"

    if emotion["C"] >= emotion["F"]:
        answer += "C"
    else:
        answer += "F"

    if emotion["J"] >= emotion["M"]:
        answer += "J"
    else:
        answer += "M"

    if emotion["A"] >= emotion["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer