import os
import fibonacci as fib

fib_series = fib.fibonacci_series(20)
print("file: ", os.path.basename(__file__))
print("fib series: ", fib_series)
