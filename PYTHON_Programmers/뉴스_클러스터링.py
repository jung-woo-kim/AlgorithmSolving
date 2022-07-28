def solution(str1, str2):
    answer = 0
    str1_dic = dict()
    str2_dic = dict()
    total_dic = dict()
    same_dic = dict()
    
    for i in range(0,len(str1)-1):
        if not('a' <= str1[i] <= 'z' or 'A' <= str1[i] <= 'Z'):
            continue
        if not('a' <= str1[i+1] <= 'z' or 'A' <= str1[i+1] <= 'Z'):
            continue
        temp = str1[i]+str1[i+1]
        temp = temp.lower()
        try:
            str1_dic[temp] += 1
        except:
            str1_dic[temp] = 1
            
        try:
            total_dic[temp] += 1
        except:
            total_dic[temp] = 1
            
    for i in range(0,len(str2)-1):
        if not('a' <= str2[i] <= 'z' or 'A' <= str2[i] <= 'Z'):
            continue
        if not('a' <= str2[i+1] <= 'z' or 'A' <= str2[i+1] <= 'Z'):
            continue
        temp = str2[i]+str2[i+1]
        temp = temp.lower()
        try:
            str2_dic[temp] += 1
        except:
            str2_dic[temp] = 1
            
        try:
            total_dic[temp] += 1
        except:
            total_dic[temp] = 1
                
    
    for item in str1_dic.keys():
        try:
            str2_dic[item] += 0
            same_dic[item] = min(str1_dic[item],str2_dic[item])
        except:
            pass

    print(str2_dic)
    print(str1_dic)
    print(total_dic)
    print(same_dic) 
    if (len(str2_dic) == 0 and len(str1_dic) == 0):
        answer = 1 *65536
        return answer
    
    
    
    t_sum = 0
    for key in total_dic.keys():
        t_sum += total_dic[key]
    
    s_sum = 0
    for key in same_dic.keys():
        s_sum += same_dic[key]
    
    answer = int((s_sum / (t_sum-s_sum)) * 65536)
    return answer

solution('handshake','shake hands')