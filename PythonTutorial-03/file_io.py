# the default open mode is "r", which is read only
f = open("binary_num.py", "r")

print ("Name of the file: ", f.name)
print ("Closed or not : ", f.closed)
print ("Opening mode : ", f.mode)

str = f.read(20)
print("read 2 result: ", str)

position = f.tell()
print("the current position of cursor: ", position)

line1 = f.readline()
print("entire line1 read: ", line1)
line2 = f.readline()
print("entire line2 read: ", line2)

position = f.tell()
print("the current position of cursor: ", position)
