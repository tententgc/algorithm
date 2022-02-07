def romanTOInt(s): 
    '''
    Convert a roman numeral to an integer
    
    :param s: the string to be converted
    :return: The last value of the list.
    '''
    case = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    solution = case[s[-1]]
    if len(s) > 1 :
        for idx in range (len(s)-2 ,-1 ,-1):
            case[s[idx]]
            if case[s[idx]] < case[s[idx+1]]: 
                solution -= case[s[idx]] 
            else:solution += case[s[idx]] 
    return solution 
a= input()
romanTOInt(a)