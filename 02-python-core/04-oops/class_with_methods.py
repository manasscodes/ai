# Class with instance variables and methods
class Student:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student()
s1.set_details("Manas", 21)
s1.display()