import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    people = []

    for __ in range(N):
        people.append(list(map(int,sys.stdin.readline().rstrip().split())))

    people.sort(key=lambda x : x[0])
    answer = N
    now_min = people[0][1]
    for i in range(1,N):
        if people[i][1] < now_min:
            now_min =  people[i][1]
        else:
            answer -= 1
    
    print(answer)