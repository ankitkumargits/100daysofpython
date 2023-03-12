print("Classes are the blueprint of the object ")

class Person:
    name = "ANKIT"
    occupation = "Software Engineer"
    age = 21
    def info(self):
        print(f"{self.name} and {self.occupation} is a member of Person")
a = Person()
print(a.name, a.occupation)
# a.name = "NoteBook"
# a.occupation = "Rapper"
# print(a.name, a.occupation)
a.info()