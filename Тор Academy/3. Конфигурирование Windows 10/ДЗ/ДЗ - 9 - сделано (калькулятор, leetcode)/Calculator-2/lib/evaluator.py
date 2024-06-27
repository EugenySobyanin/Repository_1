def Evaluate(input: str):
    operations = []
    for token in input:
        operations.append(token)
        curToken = operations[len(operations)-1]
        if curToken == "-":
            operations.pop()
            second = float(operations.pop())
            first = float(operations.pop())
            operations.append(str(first - second))
        elif curToken == "+":
            operations.pop()
            second = float(operations.pop())
            first = float(operations.pop())
            operations.append(str(first + second))
        elif curToken == "*":
            operations.pop()
            second = float(operations.pop())
            first = float(operations.pop())
            operations.append(str(first * second))
        elif curToken == "/":
            operations.pop()
            second = float(operations.pop())
            first = float(operations.pop())
            operations.append(str(first / second))
        elif curToken == "^":
            operations.pop()
            second = float(operations.pop())
            first = float(operations.pop())
            operations.append(str(first ** second))
        else:
            operations.append(operations.pop())

    return operations.pop()
