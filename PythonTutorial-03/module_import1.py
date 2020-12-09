import os
import fibonacci

fib_series = fibonacci.fibonacci_series(20)
print("file: ", os.path.basename(__file__))
print("fib series: ", fib_series)