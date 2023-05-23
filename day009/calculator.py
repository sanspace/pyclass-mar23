# add 5 2
# 7
# subtract 7 3
# 4
# multiply 5 2
# 10
# divide 10 5
# 2
# 2

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

instruction = input("Enter instruction: ")
operation, operand1, operand2 = instruction.split()
if operation == "add":
    print(add(int(operand1), int(operand2)))

