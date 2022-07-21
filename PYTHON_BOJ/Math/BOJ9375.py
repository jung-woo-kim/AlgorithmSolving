import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dic = dict()
    temp = []
    temp1 = []
    for __ in range(N):
        
        name,cloth = sys.stdin.readline().rstrip().split()
        
        temp.append(cloth)
        temp1.append(name)

        try:
            dic[cloth].append(name)
        except:
            dic[cloth] = [name]
    a = 1
    temp = set(temp)
    for c in temp:
        a*=(len(dic[c])+1)
    
    answer = 0

    answer = a-1
    
    print(answer)