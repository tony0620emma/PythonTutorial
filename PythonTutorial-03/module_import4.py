import os
from fibonacci import *

fib_20 = fibonacci(20)
fib_series = fibonacci_series(20)
print("file: ", os.path.basename(__file__))
print("fib 20 is:  ", fib_20)
print("fib series: ", fib_series)
