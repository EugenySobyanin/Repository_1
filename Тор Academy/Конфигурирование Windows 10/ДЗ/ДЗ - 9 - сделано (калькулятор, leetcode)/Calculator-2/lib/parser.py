def Parse(tokens):
    # 1 + 2 -> 1 2 +
    # ( 3 + 5 ) / ( 2 - 1 ) * 3 -> 5 3 + 2 1 - / 3 *

    stack = []
    parsed = []

    for token in tokens:
        if (token == "("):
            stack.append(token)
        elif (token == ")"):
            while (len(stack) != 0 and stack[len(stack)-1] != "("):
                parsed.append(stack.pop())
            stack.pop()
        elif (isOperator(token)):
            while (len(stack) != 0
                   and Priority(stack[len(stack)-1]) >= Priority(token)):
                parsed.append(stack.pop())
            stack.append(token)
        else:
            parsed.append(token)
    while (len(stack) != 0):
        parsed.append(stack.pop())
    return parsed


def Priority(token):
    if token == "^":
        return 5
    if token == "/":
        return 2
    if token == "*":
        return 2
    if token == "+":
        return 1
    if token == "-":
        return 1
    return 0


def isOperator(token):
    return token in "+-*/^"
