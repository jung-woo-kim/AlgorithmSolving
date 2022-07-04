def solution(id_list, report, k):
    answer = []
    
    temp = dict()
    my = dict()
    
    for id in id_list:
        temp[id] = 0
        my[id] = set()
        
    for st in set(report):
        li = st.split()
        temp[li[1]] += 1
        my[li[0]].add(li[1])
    
    for i in id_list:
        result = 0
        for u in my[i]:
            
            if temp[u]>=k:
                result +=1
                
        answer.append(result)
            
    
    return answer