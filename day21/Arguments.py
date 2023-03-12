# print("Functions arguments in python")

# def avg(a, b=1):
#     print("The average is", (a+b)/2)
    
# avg(4, 6)       # arguments in python
# avg(5)          # required arguments 
# avg(b = 6, a=4)


# # default arguments in python
# def getName(name="Hello"):      # default arguments
#     print(name+" Good Morning ")
    
# getName()
# getName("Ankit")



def avg(*num):   # arguments num is here goes with as a tuple  # you can send arguments how many you want to give to the function
    pass
    
def avg2(**num):   # arguments num is here goes with as a dictionary(other lang objects like dictionary in python key value pair)
    pass

def getName(name):
    return name
    # name

c = getName("Ankit")
print(c)