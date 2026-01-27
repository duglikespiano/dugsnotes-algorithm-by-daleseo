def isValidParantheses(string):
    parens = {"(": ")", "{": "}", "[": "]"}
    stack = []

    # Check the character of string
    # If the character is one of the opening parentheses, put it in the stack
    # If the character is one of the closing parentheses, check if that is closing bracket of last parentheses in the stack
    # If the stack is empty or the last opening parentheses and the last closing parentheses don't match, return False
    # Or return True

    # 0(n) time | 0(n) space

    for character in string:
        if character in parens:  # opening
            stack.append(character)
        else:  # closing
            if not stack or character != parens[stack.pop()]:
                # parens[stack.pop() -> stack:({[ character :}
                # or stack is empty
                return False
    return not stack


print(isValidParantheses("{([])}"))
print(isValidParantheses("{(})"))
