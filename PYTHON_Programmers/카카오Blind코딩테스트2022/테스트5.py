def solution(commands):
    answer = []

    board = [[["",[(y,x)]] for x in range(51)] for y in range(51)]

    for c in commands:
        li = c.split()
        if li[0] == "UPDATE":
            if len(li) == 4:
                for r,c in board[int(li[1])][int(li[2])][1]:
                    board[r][c][0] = li[3]
            else:
                for y in range(1,51):
                    for x in range(1,51):
                        if board[y][x][0] == li[1]:
                            board[y][x][0] = li[2]

        if li[0] == "MERGE":
            r1,c1 = int(li[1]),int(li[2])
            r2,c2 = int(li[3]),int(li[4])
            temp_li = list(set(board[r1][c1][1]+board[r2][c2][1]))
            for r,c in board[r1][c1][1]:
                board[r][c][1] = temp_li
            for r,c in board[r1][c1][1]:
                board[r][c][1]= temp_li

            if board[r1][c1][0] != "":
                for r,c in board[r1][c1][1]:
                    board[r][c][0] = board[r1][c1][0]
            elif board[r2][c2][0] != "":
                for r,c in board[r2][c2][1]:
                    board[r][c][0] = board[r2][c2][0]

        if li[0] == "UNMERGE":
            
            for r,c in board[int(li[1])][int(li[2])][1]:
                if r == int(li[1]) and c == int(li[2]):
                    pass
                else:
                    board[r][c][1] = [(r,c)]
                    board[r][c][0] = ""
            board[int(li[1])][int(li[2])][1] = [(int(li[1]),int(li[2]))]
            
        if li[0] == "PRINT":
            r1,c1 = int(li[1]),int(li[2])
            if board[r1][c1][0] != "":
                answer.append(board[r1][c1][0])
            else:
                answer.append("EMPTY")
        print(board)
    return answer

print(solution(

["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))