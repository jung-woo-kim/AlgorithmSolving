N = int(input())

fac = 1

for i in range(1,N+1):
    fac*=i

st = str(fac)

answer = 0

for i in range(len(st)-1,-1,-1):
    if st[i] == "0":
        answer+=1
    else:
        print(answer)
        exit()

print(0)