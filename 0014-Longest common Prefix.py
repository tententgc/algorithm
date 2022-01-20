def longestCommonPrefix(strs):
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
