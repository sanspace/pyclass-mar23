vowels = 'AEIOU'
name = input("Enter name: ")

for letter in name:
    if letter.upper() in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
