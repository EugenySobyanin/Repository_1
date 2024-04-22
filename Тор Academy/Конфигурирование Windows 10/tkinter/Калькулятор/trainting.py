def correct_bracket(expression):
    stack = []
    open_brackets = '([{'
    close_brackets = ')]}'
    expression = str(expression)
    for i in range(len(expression)):
        if expression[i] in open_brackets:
            stack.append(expression[i])
        elif expression[i] in close_brackets:
            if close_brackets.find(expression[i]) == open_brackets.find(stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
    return True


test1 = '([)]'


print(correct_bracket(test1))