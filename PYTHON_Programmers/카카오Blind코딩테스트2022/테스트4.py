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


def solution(numbers):
    global check
    answer = []
    nums = []
    for n in numbers:
        nums.append(bin(n)[2:])
    
    for b in nums:
        check = True
        recur(b)
        if not check:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution([42]))