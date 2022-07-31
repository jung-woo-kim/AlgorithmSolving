import heapq
import sys

N = int(sys.stdin.readline().rstrip())

plus_hq = []
len_plus = 0
minus_hq = []
len_minus = 0

zero = False

for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if temp > 0:
        heapq.heappush(plus_hq,(-temp,temp))
        len_plus += 1
    elif temp == 0:
        zero = True
       
    else:
        heapq.heappush(minus_hq,temp)
        len_minus += 1

answer = 0
t_plus = 0
t_minus = 0

while len_plus > 1:
    a = heapq.heappop(plus_hq)[1]
    b = heapq.heappop(plus_hq)[1]
    if a == 1 or b == 1:
        answer += (a + b)
    else: 
        answer += (a*b)
    len_plus -= 2

if len_plus == 1:
    t_plus = heapq.heappop(plus_hq)[1]
    len_plus -= 1

while len_minus > 1:
    a = heapq.heappop(minus_hq)
    b = heapq.heappop(minus_hq)
    answer += (a*b)
    len_minus -= 2

if len_minus == 1:
    t_minus = heapq.heappop(minus_hq)
    len_minus -= 1

if zero:
    if t_plus > 0:
        answer += t_plus
else:
    if t_plus !=0 and t_minus != 0:
        answer += max(t_plus+t_minus,t_plus*t_minus)
    elif t_plus ==0 and t_minus != 0:
        answer += t_minus
    elif t_plus !=0 and t_minus == 0:
        answer += t_plus

print(answer)


