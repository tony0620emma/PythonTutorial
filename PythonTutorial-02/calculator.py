
def Calculator(n1, n2, op):
    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2
    elif op == "/":
        result = n1 / n2
    elif op == "**":
        result = n1 ** n2
    else:
        raise Exception(f"Invalied operator {op}")
    return result
