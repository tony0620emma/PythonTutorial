
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
        raise
    return result

try:
    # see what happens if the op is something else
    result = Calculator(7, 3, "?")
except Exception as e:
    print(f"Failed to calculate: {e}")
else:
    print(f"result = {result}")
finally:
    print("I am done using calculator")


