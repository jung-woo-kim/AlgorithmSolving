import math

def solution(fees, records):
    answer = []
    car = []
    out = dict()
    for r in records:
        time,n,direction = r.split(" ")
        hh,mm = time.split(":")
        time = int(hh)*60 + int(mm)
        if direction == "IN":
            car.append([time,n])
        else:
            for c in car:
                if c[1] == n:
                    car.remove(c)
                    try:
                        out[n] += time-c[0]
                    except:
                        out[n] = time-c[0]
    
    for c in car:
        try:
            out[c[1]] += (23*60 + 59) - c[0]
        except:
            out[c[1]] = (23*60 + 59) - c[0]

    
    li = sorted(out.keys())
    
    for k in li:
        time = out[k]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            sum = fees[1]
            sum += math.ceil((time - fees[0])/fees[2])*fees[3]
            answer.append(sum)

    return answer