def solution(orders, course):
    answer = []
    
    big = dict()
    for c in course:
        big[c] = 0
    
    def dfs(depth,M,st,order,s):
        nonlocal dic
        if depth == M:
            st = "".join(sorted(st))
            try:
                dic[st] += 1
            except:
                dic[st] = 1
                
            big[M] = max(big[M],dic[st])
        for i in range(s,len(order)):
            if not visited[i]:
                visited[i] = True
                temp = st +order[i]
                dfs(depth+1,M,temp,order,i+1)
                visited[i] = False
    
    dic = dict()
    visited = [False for _ in range(10)]
    
    for o in orders:
        for c in course:
            visited = [False for _ in range(10)]
            dfs(0,c,"",o,0)
    for c in course:
        for key in dic.keys():
            if len(key) == c:
                if dic[key] == big[c] and big[c] > 1:
                    answer.append(key)
    print(big)
    answer.sort()
    return answer