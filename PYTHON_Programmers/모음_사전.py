answer = 0

def solution(word):
    global answer
    answer = 0
    alphabets = ['A','E','I','O','U']

    def DFS(string):
        global answer
        answer += 1

        if string == word:
            return True
        
        if len(string) == 5:
            return False
        
        for alpha in alphabets:
            if DFS(string+alpha) == True:
                return True 
        
    for alpha in alphabets:
        if DFS(alpha) == True:
            return answer