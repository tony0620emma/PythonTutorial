import os
import fibonacci as fib

fib_series = fib.fibonacci_series(20)
print(os.path.basename(__file__), fib_series)
