import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

if len(li) == 1:
    print(li[0])
    exit()
elif len(li) == 2:
    print(max(li[0],li[1],li[0]+li[1]))
    exit()

ds = [0 for _ in range(N)]
ds[0] = li[0]
for i in range(1,N):
    ds[i] = max(li[i],ds[i-1] + li[i])

de = [0 for _ in range(N)]
de[N-1] = li[N-1]
for i in range(N-2,0,-1):
    de[i] = max(li[i],de[i+1] + li[i])

ans = max(ds)

for i in range(1,N-1):
    ans = max(ans,ds[i-1]+de[i+1])
    


print(ans)
