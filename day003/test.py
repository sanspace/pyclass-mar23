name = input("Enter name: ")
string = input(f"{name}, Please Enter string:")
for letter in string:
   if letter.lower() in "aeiou": 
        print(f"{letter} is a vowel")
   else:
        print(f"{letter} is not a vowel")