print("Seek and Tell function in pythons")

with open("file.txt", "r") as f:
    print(type(f))
    
    f.seek(1)
    print(f.tell())    # it gives us where is the seek position
    data = f.read(5)
    print(data)
    

with open("file2.txt", "w") as f:
    f.write("Hello world!")
    f.truncate(5)   # it gives us only hello not hello world