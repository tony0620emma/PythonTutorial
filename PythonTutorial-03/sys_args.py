import sys

print("imput arguments: ", sys.argv)

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
    
    print(result)
    return result

Calculator(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])