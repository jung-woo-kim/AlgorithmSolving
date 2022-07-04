import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    temp = ''
    
    new_id = re.findall('[a-z0-9\-\_\.]',new_id)
    new_id = ''.join(new_id)
    temp = ''
    check = False
    for st in new_id:
        if st == ".":
            if not check:
                temp+="."
            check = True
        else:
            temp+=st
            check = False
            
    check = False         
    temp = ""
    for st in new_id:
        if st == ".":
            if not check:
                temp += "."
                check = True
            else:
                continue
        else:
            temp += st
            check = False
    
    new_id = temp
    
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')

    if new_id == '': new_id = 'a'
    
    new_id = new_id[0:15]
    if new_id[len(new_id)-1] == '.': new_id = new_id.rstrip('.')
    
    if len(new_id) <= 2: 
        while len(new_id) < 3: 
            new_id = new_id + new_id[len(new_id)-1]
    answer = new_id
    print(new_id)
    return answer
    
    
    
    print(new_id)
    return answer