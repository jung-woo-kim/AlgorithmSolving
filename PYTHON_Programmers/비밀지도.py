def solution(n, arr1, arr2):
    answer = []
    board1 = []
    board2 = []
    for i in range(n):
        one = bin(arr1[i])[2:]
        two = bin(arr2[i])[2:]
        one = "0"*(n-len(one)) + one
        two = "0"*(n-len(two)) + two
        board1.append(one)
        board2.append(two)

    for y in range(n):
        temp = ""
        for x in range(n):
            if board1[y][x] == '1' or board2[y][x] == '1':
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    
    return answer