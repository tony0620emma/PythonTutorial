import sys

file_name = "binary_num.py"

try:
    f = open(file_name, "r")
except FileNotFoundError:
    print(f"File {file_name} does not exist")
    sys.exit(0)

print ("Name of the file: ", f.name)
print ("Closed or not : ", f.closed)
print ("Opening mode : ", f.mode)

