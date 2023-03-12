print("Hello another one")

x = 4
print(x)

def Hello():
    global x  # global keyword is here make it any variable is global when you want to change something
    x = x + 10 # try to avoid this mistakes 
    # x = 5
    print(x)
    print(f"The Local x is {x}")
    print("Hello ANKIT")
    
    
print(f"The Global x is {x}")
Hello()
print(f"The Global x is {x}")
