answer_li = []
max = -1
def DFS(s,li,depth,n,info):
    global max
    global answer_li
    if depth == n:
        print(li)
        lion = 0
        apeech = 0
        for i in range(11):
            if info[i] == 0 and li[i] == 0:
                continue
            if info[i] < li[i]:
                lion += (10-i)
            else:
                apeech += (10-i)
        
        if lion > apeech:
            if lion-apeech > max:
                answer_li = [li]
                max = lion-apeech
            elif lion-apeech == max:
                answer_li.append(li)
        return

    for i in range(s+1,5):
        tmp = li[:]
        tmp[i] += 1
        DFS(s,tmp,depth+1,n,info)

def solution(n, info):
    answer = []
    tmp = [0 for i in range(11)]
    DFS(-1,tmp,0,n,info)
    print(answer_li)
    if len(answer_li) == 0:
        return -1
    
    return answer

solution(3,[2,1,1,1,0,0,0,0,0,0,0])