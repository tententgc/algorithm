def solution(s): 
    '''
    Given a string, return True if the string is a valid bracket sequence, and False otherwise. 
    
    The string is valid if it consists of a sequence of open and closed brackets, where every open
    bracket can be paired with a later closed bracket, and vice versa. 
    
    The string is not valid if it contains any unmatched brackets. 
    
    The string is not valid if it contains unmatched brackets that are not part of a matching pair. 
    
    The string is not valid if it contains unmatched brackets that are not part of a matching pair, and
    also contains unmatched brackets that are part of a matching pair. 
    
    The string is not valid if it contains unmatched brackets that are not part of a matching pair, and
    also contains unmatched brackets that are part of a matching pair, and also contains unmatched
    brackets that are not part of a matching pair. 
    
    The string is not valid if it contains unmatched brackets that are not part of a matching pair
    
    :param s: the string to be checked
    :return: The index of the first character of the substring.
    '''
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
