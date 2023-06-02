def solution(plans):
    answer = []
    temp = []

    for homework,start,time in plans:
        h,m = start.split(":")
        temp.append([homework,int(h)*60+int(m),int(time)])
    
    temp.sort(key=lambda x:x[1])

    plans = temp

    stopped = []
    doing = []

    for homework,start,time in plans:
        print(stopped)
        if len(doing) == 0:
            doing = [homework,start,time]
            continue
        d_homework,d_start,d_time = doing

        if d_start + d_time == start:
            answer.append(d_homework)
            
        elif d_start + d_time < start:
            answer.append(d_homework)
            rest_time = start - (d_start+d_time)
            while stopped:
                s_homework,s_start,s_time = stopped.pop()
                if s_time <= rest_time:
                    rest_time -= s_time
                    answer.append(s_homework)
                else:
                    stopped.append([s_homework,s_start,s_time-rest_time])
                    break
        else:
            stopped.append([d_homework,d_start,(d_start + d_time) - start])
        
        doing = [homework,start,time]
    
    answer.append(doing[0])

    while stopped:
        s_homework,s_start,s_time = stopped.pop()
        answer.append(s_homework)

    return answer