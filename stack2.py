def is_balanced(expr):
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ")":
            if not  stack:
                return False
            stack.pop()
    return len(stack) == 0
print(is_balanced("(())"))
print(is_balanced("(()"))
