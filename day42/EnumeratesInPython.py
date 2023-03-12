
print("Enumerate functions in python")  # it gives us a list of numbers of index numbers 

marks = [9, 5, 6, 7, 8, 4, 3, 2]

# index = 0
# for mark in marks:
#     print(index, mark)
#     if (index == 3):
#         print("Ankit Awesome")
#     index += 1

# it gives me an index number 
    
for index, mark in enumerate(marks, start=1):
    print(index, mark)
    if (index == 3):
        print("Ankit Awesome")

