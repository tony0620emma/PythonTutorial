

def fibonacci(n):
    """ Get n-th number of the fibonacci series. """
    f2, f1 = 0, 1
    f = f2 + f1
    if n <= 0:
        return f2
    elif n == 1:
        return f1

    for _ in range(2, n + 1):
        f = f2 + f1
        f2, f1 = f1, f

    return f

def fibonacci_series(n):
    """ Get fibonacci series up to n-th number """
    if n < 0:
        n = 0
    result = []
    for i in range(n):
        result.append(fibonacci(i))
    return result

if __name__ == "__main__":
    for i in range(10):
        x = input("Please input something:")
        print(f"your input in {i} is {x}")