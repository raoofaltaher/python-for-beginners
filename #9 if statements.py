# if statement= a block of code execute if its condition is true

age = int(input("How old are you:? "))

if age == 100:
    print("You are a century old: ")
elif age >= 18:
    print("you are an adult: ")
elif age < 0:
    print("you haven't been born yet: ")
else:
    print("you are a child: ")

