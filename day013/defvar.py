def greet(name="there", greeting="Hi"):
    print(f"{greeting} {name}!")

greet("Subi", "hello")
greet(greeting="hi", name="Arun")
greet(greeting="howdy")
greet()

user_input = input("Enter name: ")
greet(name=user_input)