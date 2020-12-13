
def function(a, b):
    print("inside  id: a = ", id(a), ", id: b = ", id(b))
    a = a + 5
    b = b + 3
    print("final   id: a = ", id(a), ", id: b = ", id(b))

a1 = 5
b1 = 10
print("outside id: a = ", id(a1), ", id: b = ", id(b1))
function(a1, b1)
