
file_name = "binary_num.py"

try:
    f = open(file_name, "r")
except (FileNotFoundError, ZeroDivisionError) as e:
    print("File does not exist, or divided by zero")
    print("Exception: ", e)
else:
    # the else block is executed only when no exception catched
    print ("Name of the file: ", f.name)
    print ("Closed or not : ", f.closed)
    print ("Opening mode : ", f.mode)
    f.close()
finally:
    # the finally block is executed no matter what happened in the try block
    print ("Leaving this try block")
