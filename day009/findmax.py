def maximum(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

numbers = [2, 4, 6, 1, 3, 9]
print(maximum(numbers))
print(maximum([1, 2, 3]) + maximum([5, 8, 11]))