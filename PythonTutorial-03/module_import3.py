import os
from fibonacci import fibonacci_series

fib_series = fibonacci_series(20)
print(os.path.basename(__file__), fib_series)
