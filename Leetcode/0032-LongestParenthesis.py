def longest(s):
    stack = []
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
            else:
                if s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
    if len(stack) == 0:
        max_len = len(s)
    else:
        a = len(s)
        while len(stack) != 0:
            b = stack.pop()
            max_len = max(max_len, a - b - 1)
            a = b
        max_len = max(max_len, a)
    return max_len

s = "(()" 
print(longest(s))