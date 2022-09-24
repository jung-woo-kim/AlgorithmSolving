from collections import deque



def direction_to_str(i):
    if i == 0:
        return "r"
    if i == 1:
        return "d"
    if i == 2:
        return "l"
    if i == 3:
        return "u"

def solution(n, m, x, y, r, c, k):
    board = [["" for _ in range(m)] for __ in range(n)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    li = []
    def BFS(sy,sx):
        q = deque()
        q.append((sy,sx,""))

        while q:
            ty,tx,st = q.popleft()
            if len(st) == k:
                if ty ==r-1 and tx ==c-1:
                    li.append(st)
            if len(st) > k:
                return

            for i in range(4):
                ny = ty + dy[i]
                nx = tx + dx[i]

                if 0<=ny<n and 0<=nx<m:
                    tmp = st+direction_to_str(i)
                    if board[ny][nx] == "":
                        board[ny][nx] = tmp
                        q.append((ny,nx,tmp))
                    for j in range(min(len(board[ny][nx]),len(tmp))):
                        if board[ny][nx][j] > tmp[j]:
                            board[ny][nx] = tmp
                            q.append((ny,nx,tmp))
                            break
                        elif board[ny][nx][j] == tmp[j]:
                            pass
                        else:
                            break
    BFS(x-1,y-1)
    print(board)
    li.sort()
    if len(li) == 0:
        return "impossible"
    return li[0]

print(solution(
3, 4, 2, 3, 3, 1, 5))
