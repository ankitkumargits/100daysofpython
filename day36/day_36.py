print("try exception in python")

n = input("Enter the number is: => ")


try: 
    for i in range(1, 11):
        print(f"{n} X {i} = {int(n)*i}")
except:   # you can use multiple exceptions handlers in python here
    print("invalid inputs")
    
print("some imp lines")
print("End of program")



