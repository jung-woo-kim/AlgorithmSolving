from collections import defaultdict
from itertools import product
import bisect

def solution(info, query):
    answer = []
    infoMap = defaultdict(list)
    all = list(product((True,False),repeat=4))
    for inf in info:
        inf = inf.split()
        for a in all:
            key = ''.join(inf[i] if a[i] else "-" for i in range(4))
            infoMap[key].append(int(inf[-1]))
    for key in infoMap.keys():
        infoMap[key].sort()
    
    for q in query:
        l,_,j,_,c,_,f,n = q.split()
        key = l+j+c+f
        i = bisect.bisect_left(infoMap[key],int(n))
        answer.append(len(infoMap[key])-i)
    
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50","java backend junior pizza 150"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])