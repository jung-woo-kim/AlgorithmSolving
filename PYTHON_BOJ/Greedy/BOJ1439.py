import sys

S = sys.stdin.readline().rstrip()

zero = 0
one = 0

now = "-1"

for i in range(len(S)):
    if S[i] == now:
        pass
    else:
        now = S[i]
        if S[i] == "0":
            zero += 1
        else:
            one += 1

print(zero)
print(one)