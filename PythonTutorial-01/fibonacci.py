f_2 = 0
f_1 = 1

for _ in range(2, 10):
    f = f_2 + f_1
    f_2 = f_1
    f_1 = f

print(f"fibonacci result = {f}")
