
# f = open("myFile.txt2", "r")  # like r have in python other methods like w, a, x, rt, rb 
# print(f.read())
# f.close()


# f = open("myFile2.txt", "w")
# f.write("hello world")
# f.close()


with open("myFile2.txt", "w") as f:  # in this no need to close the file
    f.write("with methods in python of file handling")


