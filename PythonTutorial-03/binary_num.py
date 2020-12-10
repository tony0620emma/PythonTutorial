# function bin(n) can convert n to a binary number, such as 0b11010
print(bin(77))
print(bin(38))
print(bin(77 >> 2)) # right shift 2 bits
print(bin(38 << 2)) # left shift 2 bits
print(bin(77 | 38)) # or them
print(bin(77 & 38)) # and them
print()

# better formatting
print("{0:08b}".format(77))
print("{0:08b}".format(38))
print("{0:08b}".format(77 >> 2)) # right shift 2 bits
print("{0:08b}".format(38 << 2)) # left shift 2 bits
print("{0:08b}".format(77 | 38)) # or them
print("{0:08b}".format(77 & 38)) # and them
print()

# {} places a variable to a string
# 0 takes the argument at position 0
# : adds formatting options
# 08 formats the number to 8 digits with 0 padded to the left
# b means using binary representation

# f-strings
print(f"{77:08b}")
