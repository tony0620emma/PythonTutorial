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
        # raise a NameError here
        raise NameError("A name error")
    return result

def ChainCalculator(n1, n2, op):
    try:
        result = Calculator(n1, n2, op)
    except NameError as ne:
        # chaining the exception here
        raise RuntimeError("Chaining this message to upper stack") from ne
    else:
        return result

try:
    # see what happens if the op is something else
    result = ChainCalculator(7, 3, "?")
except Exception as e:
    print(f"Failed to calculate: {e}")
else:
    print(f"result = {result}")
finally:
    print("I am done using calculator")
