import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.findall("[a-z0-9\-_.]", new_id)
    
    new_id = ''.join(new_id)

    temp = ""

    for s in new_id:
        if len(temp) >= 1:
            if temp[-1] == "." and s == ".":
                continue
        temp += s
    new_id = temp

    if new_id == ".":
        new_id = ""
    elif len(new_id) > 0:    
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    if new_id == "":
        new_id = "a"
    
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if len(new_id) == 1:
        new_id = new_id*3
    
    if len(new_id) == 2:
        new_id += new_id[-1]

    answer = new_id
    return answer