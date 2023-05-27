def solution(wallpaper):
    max_x = 0
    min_x = 51
    max_y = 0
    min_y = 51

    for y,row in enumerate(wallpaper):
        for x, r in enumerate(row):
            if r == "#":
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x

    answer = [min_y,min_x,max_y+1,max_x+1]


    return answer