import os
from fibonacci import fibonacci_series

fib_series = fibonacci_series(20)
print("file: ", os.path.basename(__file__))
print("fib series: ", fib_series)
