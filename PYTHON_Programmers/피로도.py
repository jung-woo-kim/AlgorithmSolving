answer = 0
def solution(k, dungeons):
    answer = 0
    visited = [False for _ in range(len(dungeons))]
    DFS([],dungeons,0,len(dungeons),visited,k)
    return answer

def DFS(li,dungeons,depth,n,visited,k):
    global answer
    if depth == n:
        max_dungeons = 0
        for min,piro in li:
            print(min)
            if k < min:
                break
            k -= piro
            max_dungeons += 1

        print(max_dungeons)
        answer = max(answer,max_dungeons)
        return 

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            li.append(dungeons[i])
            DFS(li,dungeons,depth+1,n,visited,k)
            li.pop()
            visited[i] = False