import sys

string = sys.stdin.readline().rstrip()

bomb = sys.stdin.readline().rstrip()

stack = []

for i in range(len(string)):
    stack.append(string[i])

    if len(stack) >= len(bomb):
        if "".join(stack[-len(bomb):]) == bomb:
            for j in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))