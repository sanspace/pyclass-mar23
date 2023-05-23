# count the no of vowels in a given name

vowels = 'aeiou'

counter = 0
for char in 'subanghi':
    if char in vowels:
        counter = counter + 1

print(counter)
