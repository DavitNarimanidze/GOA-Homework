def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b == 0:
            return "cannot divide by zero"
        return a / b
    else:
        return "invalid operator"
    