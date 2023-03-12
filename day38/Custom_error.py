print("Custom error message")

a = int(input("Enter a number between 5 and 9 => "))

if(a <5 or a >9):
    raise ValueError("Value should be between 5 and 9")

print("You can make custom error messages using the following commands")

