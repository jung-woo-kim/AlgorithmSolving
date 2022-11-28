n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
tmp,ans = [],set()

def bt(idx,cnt):
    if cnt==m:
        ans.add(tuple(tmp))
        return
    
    cnt+=1
    for i in range(idx,n):
        tmp.append(arr[i])
        bt(i+1,cnt)
        tmp.pop()
bt(0,0)
for i in sorted(list(ans)):
    print(*i)