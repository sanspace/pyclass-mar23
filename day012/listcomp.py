# # 1, 10
# numbers = list(range(1,11))
# print(numbers)
# odd_numbers = list(range(1,11,2))
# print(odd_numbers)
# even_numbers = list(range(0,11,2))
# print(even_numbers)

# numbers = [x for x in range(1,11)]
# print(numbers)

name = 'subanghi'
vowels = [x.upper() for x in name if x.lower() in 'aeiou']
print(vowels)