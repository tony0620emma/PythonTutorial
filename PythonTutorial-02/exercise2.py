
def Calculator(n1, n2, op):
    result = None
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
        print(f"undefined operator {op}")
    
    return result

print(Calculator(15, 5, "+"))
print(Calculator(15, 5, "-"))
print(Calculator(15, 5, "*"))
print(Calculator(15, 5, "/"))
print(Calculator(15, 5, "**"))