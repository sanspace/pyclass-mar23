def add_(): # anti pattern
    x = int(input('Enter x '))
    y = int(input('Enter y '))
    print(x + y)

# add_()

# 5, 4, 6

def add(x, y):
    return x + y

print(add(add(5, 4), 6))

