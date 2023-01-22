check = True

def recur(li):
    global check
    
    if "1" in li:
        if len(li) >= 3:
            if li[len(li)//2] == "0":
                check = False
                return

        recur(li[:len(li)//2])
        recur(li[len(li)//2+1:])

def to_bin(n):
    s = bin(n)[2:]
    for i in range(51):
        if 2**i-1 >= len(s):
            length = 2**i-1
            break
    return ("0" * (length - len(s)))+ s

def solution(numbers):
    global check
    answer = []
    nums = []
    for n in numbers:    
        nums.append(to_bin(n))
    

    for b in nums:
        check = True
        recur(b)
        if not check:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution([7,42,5]))