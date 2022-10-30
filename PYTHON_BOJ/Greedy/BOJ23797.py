import sys

S = sys.stdin.readline().rstrip()

K_frog = 0
P_frog = 0
max_k = 0
max_p = 0
for s in S:
    if s == "K":
        if P_frog > 0:
            P_frog -= 1
            K_frog += 1
        else:
            K_frog += 1
        
    else:
        if K_frog > 0:
            K_frog -= 1
            P_frog += 1
        else:
            P_frog += 1

print(K_frog+ P_frog)

#print(max(len(K),len(P)))