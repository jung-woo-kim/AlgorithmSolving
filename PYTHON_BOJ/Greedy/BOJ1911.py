import sys

N,L = map(int,sys.stdin.readline().rstrip().split())

water = []

for _ in range(N):
    start,end = map(int,sys.stdin.readline().rstrip().split())
    water.append((start,end))

water.sort()

answer = 0
last_wood = -1

for i in range(N):

    if last_wood >= water[i][1]:
        pass
    else:
        if last_wood < water[i][0]:
            tmp = (water[i][1] - water[i][0]) // L
            if (water[i][1] - water[i][0]) % L == 0:
                answer += tmp
                last_wood = water[i][0] + tmp*L
            else:
                answer += (tmp+1)
                last_wood = water[i][0] + (tmp+1)*L

        else:
            tmp = (water[i][1] - last_wood) // L
            if (water[i][1] - last_wood) % L == 0:
                answer += tmp
                last_wood += tmp*L
            else:
                answer += (tmp+1)
                last_wood += (tmp+1)*L
            
print(answer)