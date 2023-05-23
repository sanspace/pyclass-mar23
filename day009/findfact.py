def factorial(number):
    fact = 1
    for n in range(1, number+1):
        fact = fact * n
    return fact

number = int(input("Enter number: "))
print(factorial(number))
result = factorial(5) + 2
print(result)
