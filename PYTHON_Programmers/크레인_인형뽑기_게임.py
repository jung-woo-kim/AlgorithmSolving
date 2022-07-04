def solution(board, moves):
    answer = 0
    basket = []
    basket_num = 0
    for m in moves:
        doll = 0
        for i in range(len(board)):
            if board[i][m-1] != 0:
                doll = board[i][m-1]
                board[i][m-1] = 0
                break
        if doll != 0:
            print(doll)
            if basket:
                if basket[basket_num-1] == doll:
                    answer += 2
                    basket.pop()
                    basket_num-=1
                else:
                    basket.append(doll)
                    basket_num+=1
            else:
                basket.append(doll)
                basket_num+=1
    return answer