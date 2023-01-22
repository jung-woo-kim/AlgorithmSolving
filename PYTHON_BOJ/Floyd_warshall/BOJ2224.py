import sys

input = sys.stdin.readline

N = int(input().strip())
props = [[False for _ in range(52)] for __ in range(52)]  # P(행) -> Q(열)가 참이라면 True


# A : 65 ~ Z : 90 -> idx : 0 ~ 25
# a : 97 ~ z : 122 -> idx : 26 ~ 51

def Alpha2Idx(alpha):
    asciiNum = ord(alpha)  # Ascii2Num
    if 65 <= asciiNum <= 90:
        return asciiNum - 65
    return asciiNum - 71


def Idx2Alpha(idx):
    if 0 <= idx <= 25:
        return chr(idx + 65)  # Num2Ascii
    return chr(idx + 71)


for _ in range(N):  # 주어진 명제들 입력 받기
    P, __ , Q = map(str, input().split())
    if P != Q:
        props[Alpha2Idx(P)][Alpha2Idx(Q)] = True

# 삼단 논법 적용
for P in range(52):
    for Q in range(52):
        for R in range(52):
            if P == Q or Q == R or R == P:
                continue
            if props[Q][P] and props[P][R]:  # 삼단 논법
                props[Q][R] = True

# 참인 명제들 저장
proofs = []
for P in range(52):
    for Q in range(52):
        if P != Q and props[P][Q]:
            proofs.append((P, Q))

# 출력
print(len(proofs))
for P, Q in proofs:
    print(Idx2Alpha(P) + " => " + Idx2Alpha(Q))