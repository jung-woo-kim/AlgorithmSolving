def solution(park, routes):
    for x,row in enumerate(park):
        for y,r in enumerate(row):
            if r == "S":
                nx = x
                ny = y

    for route in routes:
        d,s = route.split()
        tx = nx
        ty = ny
        line = ""
        try:
            if d == "E":
                ty += int(s)
                for i in range(1,int(s)+1):
                    line += park[nx][ny+i]
            if d == "W":
                ty -= int(s)
                for i in range(1,int(s)+1):
                    line += park[nx][ny-i]
            if d == "N":
                tx -= int(s)
                for i in range(1,int(s)+1):
                    line += park[nx-i][ny]
            if d == "S":
                tx += int(s)
                for i in range(1,int(s)+1):
                    line += park[nx+i][ny]
            
            if tx < 0 or ty < 0:
                continue
        except:
            continue
        
        
        if line.find("X") == -1:
            nx = tx
            ny = ty


    answer = [nx, ny]

    return answer