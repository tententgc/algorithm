def makeGood(s):
    stack = []
    for i in s: 
        if stack and abs(ord(i) - ord(stack[-1])) == 32: 
            stack.pop()
        else: 
            stack.append(i)
    return "".join(stack) 


print(makeGood("abBAcC"))