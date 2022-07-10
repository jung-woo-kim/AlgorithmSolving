import sys

x,y,w,h = map(int,sys.stdin.readline().rstrip().split())

m = 1e9

m= min(m,y)
m= min(m,x)
m= min(m,w-x)
m= min(m,h-y)

print(m)