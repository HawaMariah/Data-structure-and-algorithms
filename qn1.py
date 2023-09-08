def is_balanced(string):
    stack = []

    opening_brackets = {"{", "(", "["}
    closing_brackets = {"}", ")", "]"}
    brackets  = {')': '(', '}': '{', ']': '['}

    

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != brackets[char]: 
                return False 
            stack.pop()  
    
    return len(stack) == 0 

# test
print(is_balanced("()"))  # True
print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False
print(is_balanced("([)]"))  # False


