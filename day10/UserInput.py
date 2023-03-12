# name = input("Enter your name => ")
# print(name)

num1 = input("Enter your number 1 ")
num2 = input("Enter your number 2 ")

try:
    sum = int(num1) + int(num2)
    print("your num1 and num2", num1, num2, "Your sum is: ", sum)
except:
    print('An exception occurred')
