def find_len(my_list):
    length = 0
    for elem in my_list:
        length = length + 1
    return length

def find_max(numbers):
    max_ = 0
    for number in numbers:
        if number > max_:
            max_ = number
    return max_

numbers = [5,6,7]
print(find_len(numbers)) # should print 3
names = ['hi', 'hello']
print(find_len(names)) # should print 2
name = "subanghi"
print(find_len(name))