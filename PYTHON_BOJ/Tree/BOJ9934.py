import sys

N = int(sys.stdin.readline().rstrip())

inorder = list(map(int,sys.stdin.readline().rstrip().split()))

tree = [[] for _ in range(N)]

def makeTree(arr, x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)

makeTree(inorder,0)

for i in range(N):
    print(*tree[i])