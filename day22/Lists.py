print("Lists in Python")

l = [6, 7, 1, 10, 6]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

if 7 in l:
    print("Yes")
else: 
    print("No")
    
print(l)
print(l[:])
print(l[1:])
print(l[1:-1]) # len(l)-1
print(l[1:4])# start index and last index
print(l[1:5:2])   # jumped index in python lists