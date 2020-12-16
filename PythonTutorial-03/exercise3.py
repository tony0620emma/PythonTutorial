# This is closed brackets
input1 = "[[[[[[[[[[[[[[[[[[[[][[[[[[[[[[][[[[[[[[[[[[[[[[][[[[[[[[[[[[[]]]]]]]]]]][[[[[[[[[[[[[[][[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]"
# This is closed brackets
input2 = "[[[[[[[[[[[[[[[[[]]]]]]]]][[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]][[[[[[[[[[[[][][][][][[[[[[[[[[[[[]]]]]]]]]]]]]]]]][][]]]]]]][][]]]]]]]]]]]]]]]]]]]]]]]]]][[[[[[[]]]]]][[[[[]][][][][][][]]]]]]]"
# This is not close brackets
input3 = "[[[[[[][][[[[[[[[[[[[[[][][[][][][][][][]]]]][[[[[[[[[[[[[[][]]]]]]]]]]]]][[[[[[[[[][][]]]]]]]]]]][]]]]]]]]]][][[[[][]]]][][][]]]]"
# This is not close brackets
input4 = "[[[[[[[[[[[[[[][]]]]]]]]]][[[[[[[[[[[[[[[[[[[[]]]]]]]]][[[[[[[[[[[[[[][][][][][][[]]]]]]]]]]]]]]]]]][][[[[[[[[[[[[[[[][][][][][][]]]]]][[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]"

def IsCloseBrackets(input):
    count = 0
    for i in range(len(input)):
        if input[i] == "[":
            count = count + 1
        elif input[i] == "]":
            count = count - 1
        else:
            print(f"illegal input {input[i]}")
            return
        if count < 0:
            print(f"Too many close bracket at {i}")
            return

    if count == 0:
        print("Bracket is Closed!")
    else:
        print("Bracket is not Closed.")

IsCloseBrackets(input1)
IsCloseBrackets(input2)
IsCloseBrackets(input3)
IsCloseBrackets(input4)
