n, k = map(int, input().split())
lst1 = input()
lst2 = input()
lst = [lst1, lst2]
visited = [[0 for i in range(n)] for _ in range(2)]
visited[0][0] = 1

def bfs():
    q = []
    q2 = []
    q2.append([0, 0])
    remove = 0
    while q2:
        now_idx, lst_num = q2.pop(0)
        # print("now_idx %d, lst_num %d" % (now_idx, lst_num))
        if now_idx + 1 >= n or now_idx + k >= n:
            return 1
        if lst[lst_num][now_idx + 1] == '1' and visited[lst_num][now_idx + 1] == 0:
            visited[lst_num][now_idx + 1] = 1
            q.append([now_idx + 1, lst_num])
        if now_idx - 1 > remove and lst[lst_num][now_idx - 1] == '1' and visited[lst_num][now_idx - 1] == 0:
            visited[lst_num][now_idx - 1] = 1
            q.append([now_idx - 1, lst_num])
        if lst[(lst_num + 1) % 2][now_idx + k] == '1' and visited[(lst_num + 1) % 2][now_idx + k] == 0:
            visited[(lst_num + 1) % 2][now_idx + k] = 1
            q.append([now_idx + k, (lst_num + 1) % 2])
        if not q2:
            q2 = q
            q = []
            remove += 1
    return 0

print(1 if bfs() else 0)