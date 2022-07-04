def solution(N, stages):
    answer = []
    fail = dict()
    dic = dict()
    for i in range(1,N+2):
        fail[i] = 0
        dic[i] = 0
    
    for s in stages:
       dic[s] += 1
       
    
    for i in range(1,N+2):
        sum = 0
        for j in range(i,N+2):
            sum += dic[j]
        if sum == 0:
            fail[i] =0
        else:
            fail[i] = dic[i]/sum
    
    sorted_dict = sorted(fail.items(), key = lambda item: item[1], reverse = True)
  
    for s in sorted_dict:
         if s[0] != N+1:
                answer.append(s[0])
    return answer