def longestCommonPrefix(strs):
    '''
    Find the longest common prefix of two strings
    
    :param strs: a list of strings
    :return: The longest common prefix of the two strings.
    '''
    q=""
    str1, str2 = min(strs), max(strs) 
    i=0
    while i < len(str1):
        if str1[i] != str2[i]:
            str1 = str1[:i]
            break
        i +=1
    return str1

print(longestCommonPrefix(["cir", "car"]))
