import sys

Rh,Rv,Sh,Sv = map(int,sys.stdin.readline().rstrip().split())

n = int(sys.stdin.readline().rstrip())

answer = 1e9

def calc(original,diff):
    if original <= diff:
        return 1
    else:
        if original % diff > 0:
            return original//diff + 1
        else:
            return original//diff

for _ in range(n):
    rh,rv,sh,sv,p = map(int,sys.stdin.readline().rstrip().split())

    h_num = 0
    v_num = 0

    temp1 = calc(Rh,rh)

    temp2 = calc(Sh,sh) 

    h_num = max(temp1,temp2)
    

    temp1 = calc(Rv,rv)

    temp2 = calc(Sv,sv)

    v_num = max(temp1,temp2)

    answer = min(answer,(h_num*v_num)*p)


    temp1 = calc(Rh,rv)

    temp2 = calc(Sh,sv)
    
    h_num = max(temp1,temp2)


    temp1 = calc(Rv,rh)

    temp2 = calc(Sv,sh)

    v_num = max(temp1,temp2)


    answer = min(answer,(h_num*v_num)*p)



print(answer)


    
