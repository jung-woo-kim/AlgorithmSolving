answer_li = []
max = -1
def DFS(li,i,n,info):
    global max
    global answer_li
    if i == 11:
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
            tmp = li[:]
            if n != 0:
                for i in range(10,0,-1):
                    if tmp[i] == 0:
                        tmp[i] = n
                        break
            if lion-apeech > max:
                answer_li = [tmp]
                max = lion-apeech
            elif lion-apeech == max:
                answer_li.append(tmp)
        return

    if info[i] < n:
        li.append(info[i]+1)
        DFS(li,i+1,n-(info[i]+1),info)
        li.pop()
    
    li.append(0)
    DFS(li,i+1,n,info)
    li.pop()

def solution(n, info):
    global max
    global answer_li
    
    answer_li = []
    max = -1
    DFS([],0,n,info)
    if len(answer_li) == 0:
        return [-1]
    answer_li.sort(key=lambda x: x[::-1], reverse=True)
    
    return answer_li[0]

solution(5,[2,1,1,1,0,0,0,0,0,0,0])