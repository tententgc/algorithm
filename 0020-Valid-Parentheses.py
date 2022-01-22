def solution(s): 
    q=[]
    for i in s: 
        if i in "([{": 
            q.append(")]}"["([{".find(i)]) 
        else: 
            if i==q[-1]:
                q.pop()
            else: 
                return "false" 
    return "true"
    
    
print(solution("()[]{}"))
