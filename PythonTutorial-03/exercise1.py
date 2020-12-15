# base64
base64_encode = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

"""
              a            b           c
        | 11010110  |  10110100  | 01011011 |
    =>  | 110101 | 101011 | 010001 | 011011 |
            w        x         y        z
"""

ascii_string = "Hello World! This is Tony Chuang from Taiwan."

# get the length of the string
str_len = len(ascii_string)

result_list = []
# devide into groups, each with 3 characters
for i in range(0, str_len , 3):
    a = ord(ascii_string[i])
    b = ord(ascii_string[i + 1])
    c = ord(ascii_string[i + 2])
    w = a >> 2
    x = (a & 3) + ((b & 240) >> 4)
    y = ((b & 15) << 2) + ((c & 192) >> 6)
    z = c & 63

    # encode the resulted binary value
    s1 = base64_encode[w]
    s2 = base64_encode[x]
    s3 = base64_encode[y]
    s4 = base64_encode[z]
    
    result_list.append(s1)
    result_list.append(s2)
    result_list.append(s3)
    result_list.append(s4)

result_string = "".join(result_list)
print(result_list)
print(result_string)