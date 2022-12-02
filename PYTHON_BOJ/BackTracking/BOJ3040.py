import sys

nanjangyee = []

for i in range(9):
    nanjangyee.append(int(sys.stdin.readline().rstrip()))

sum_nanjanyee = sum(nanjangyee)

for i in range(8):
    for j in range(i+1,9):
        if sum_nanjanyee - nanjangyee[i] - nanjangyee[j] == 100:
            for num in nanjangyee:
                if num != nanjangyee[i] and num != nanjangyee[j]:
                    print(num)
            exit()
