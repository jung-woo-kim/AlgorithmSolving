import math
def convert(num,base):
    q,r = divmod(num,base)
    if q == 0:
        return str(r)
    else:
        return convert(q,base) + str(r)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
        
    return True # 소수임

def solution(n, k):
    answer = 0
    
    k_num = convert(n,k)
    ks = k_num.split("0")
    
    for k in ks:
        if k == "":
            continue
        if is_prime_number(int(k)):
            answer += 1

    
    return answer