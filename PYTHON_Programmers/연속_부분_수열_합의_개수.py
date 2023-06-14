def solution(elements):
    s = set(elements)
    dp = elements[:]
    el = elements + elements

    for i in range(2,len(elements)):
        for j in range(len(elements)):
            dp[j] = dp[j] + el[j+i-1]
            s.add(dp[j])
    
    return len(s) + 1